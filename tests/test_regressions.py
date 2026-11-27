import json
from pathlib import Path
import tempfile
import unittest
from _load import load, example

ue = load('founder-cfo', 'unit_economics')
panel = load('founder-consumer', 'panel')
pricing = load('founder-pricing', 'van_westendorp')
plan = load('founder-plan', 'compile')

class Regressions(unittest.TestCase):
    def numbers(self):
        return json.loads(Path(example('founder-cfo','example.json')).read_text(encoding='utf-8'))

    def test_nonfinite_negative_and_missing_costs(self):
        for key, value in [('price',float('nan')),('days_per_month',0),('plan_per_day',-1),('capacity_per_day',float('inf')),('variable',None)]:
            s = self.numbers()
            s[key] = value
            with self.assertRaises(ue.NumbersError, msg=key):
                ue.analyse(s)
        with self.assertRaises(ue.NumbersError):
            ue.analyse(self.numbers(), volume=-1)

    def test_panel_reinit_and_bad_save_preserve_data(self):
        with tempfile.TemporaryDirectory() as td:
            d = str(Path(td) / 'panel')
            panel.init(d, example('founder-consumer','customer.example.json'), example('founder-consumer','pitch.example.md'), n=3, seed=1)
            good = json.dumps({'id':'P001','buys':False,'reason_code':'price','reason':'synthetic test fixture'})
            panel.save(d, 'P001', good)
            p = Path(d) / 'answers/P001.json'
            before = p.read_bytes()
            for bad in ('[]','{"id":"P001","buys":"maybe"}'):
                with self.assertRaises(panel.PanelError):
                    panel.save(d, 'P001', bad)
            self.assertEqual(p.read_bytes(), before)
            with self.assertRaises(panel.PanelError):
                panel.init(d, example('founder-consumer','customer.example.json'), example('founder-consumer','pitch.example.md'))
            self.assertEqual(p.read_bytes(), before)
            with self.assertRaises(panel.PanelError):
                panel.write_briefs(d, wave=0)

    def test_pricing_nonfinite_and_unbounded_grid(self):
        self.assertIsNone(pricing._f('inf'))
        with self.assertRaises(pricing.PricingError):
            pricing.analyse([(1,2,3,4)] * 5, step=-1)
        with self.assertRaises(pricing.PricingError):
            pricing.analyse([(1,2,3,4)] * 5, step=1e-10)

    def test_missing_panel_is_not_a_complete_verdict(self):
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / 'numbers.json').write_text(json.dumps(self.numbers()))
            self.assertEqual(plan.verdict(td)[0], 'Incomplete')
            with self.assertRaises(ValueError):
                plan.verdict(td, float('nan'))
