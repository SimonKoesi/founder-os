
# founder-consumer

The craziest part of the pack. Instead of guessing whether people will buy, you
ask a hundred of them, each one an independently evaluated scenario playing a specific buyer drawn from
your target customer. You are the moderator. You never answer for a buyer.

What the user typed after `$founder-consumer`: `the user request`

## The tool

All bookkeeping goes through `panel.py` in this skill's folder:

```bash
python3 "<skill-directory>/panel.py" <command>
```

Below, `PANEL` means exactly that. Resolve the script path from this method's
directory. State lives in `founder/panel/` inside the user's project.

## Step 1: the target customer

Write `founder/customer.json` (shape: `customer.example.json` in this folder):

- `business`, and `target`: who the customer is, in one specific line.
- `segments`: 2 to 4 groups with a `share` and an `income` range [low, high].
- `behaviours`: 4 to 8 buying behaviours with a `share` and a `how` line
  (daily regular, deal hunter, reads every review, loyal to a competitor...).
- `objections`: the 4 to 8 doubts this kind of buyer really has.
- `habits` (optional): everyday context lines that make a buyer concrete.

Ground it in something real. Use what the user knows about their customers, and
if `$founder-competitors` ran, the complaints in `founder/competitors.md`. If the
user has real customer data (interviews, reviews, survey answers), prefer it to
your guesses and say which parts are guesses. Show the user the profile in a few
lines and let them correct it before you deal: a wrong customer makes the whole
panel wrong.

## Step 2: the pitch

Write `founder/pitch.md`: what a buyer would actually see. The product, the price,
where and how to get it, any opening offer. Three to six plain lines, no
superlatives, nothing the business cannot deliver. Every buyer sees exactly this.

## Step 3: deal and run

Use a new panel directory for each pitch version; init refuses existing state.
Start with 20 cards, recording the seed and pitch. `--quick` is a workflow shorthand,
not a Python CLI flag. Translate it to `--n 20`.

```sh
python <skill-directory>/panel.py --dir founder/panel init --customer founder/customer.json --pitch founder/pitch.md --n 20 --seed 7
python <skill-directory>/panel.py --dir founder/panel prompts --wave 3
python <skill-directory>/panel.py --dir founder/panel check
python <skill-directory>/panel.py --dir founder/panel tally
```

The tool generates briefs, never model answers. Independent buyer agents require
authorization and available tools; size waves to actual concurrency and agreed cost.
Without these, prepare briefs or import real research; report the panel as pending.
Never manufacture answers in the moderator session or present fixtures as research.
Retry missing/broken answers once, then disclose exclusions. `save` accepts an
existing buyer's own response; it validates before replacing a file.

## Step 4: read it to the user

`PANEL tally` writes `founder/panel/results.md` and `results.json`. Give the user:

1. The headline: "40 buy · 60 pass" and the buy rate.
2. Who buys and who doesn't: the segment and behaviour rows that differ most.
3. Why they pass: the top three reasons with one quote each, as written.
4. What would flip a no: the most repeated answers.
5. One sentence on what to change before spending money, and which skill does it
   (pricing, offer, marketing).

## Honest limits, say them once

These are simulated buyers. They are good at surfacing objections, segments and
wording you had not thought of, and bad at predicting real conversion: language
models lean agreeable, so do not treat the buy rate as a forecast or calibrated bound. Confirm the big
calls with real people (a waitlist, a pre-sale, a landing page with a price)
before signing anything. Do not present panel quotes as customer testimonials.

## The brief every buyer gets

`panel.py` fills the card into a fixed template (see `BRIEF` in the script): who
the buyer is (name, age, segment, income, buying behaviour, a habit, the doubt
that comes to mind), the pitch word for word, an instruction not to be agreeable
and not to invent facts, and the exact JSON to write: buys, purchases in the first
month, a reason code, the reason in their own voice, their main objection, what
would change their mind, and four price answers (too cheap, a bargain, getting
expensive, too expensive). Never edit a brief for one buyer.

## Output

`founder/customer.json`, `founder/pitch.md`, `founder/panel/` (cards, briefs,
answers, results). Next: `$founder-pricing` reads the price answers,
`$founder-offer` and `$founder-marketing` read the objections.
