# Run rules and progression

**Tools ▸ Dungeon Shooter Maker ▸ Run Rules** holds the rules the whole run shares: what the hero starts with, what
rooms pay, what things cost, how curse and flair work, which enemies can be elite, which offer opens when, and the
lobby between runs.

<!-- TODO(screenshot): Run Rules window, saved as assets/images/run-rules.png -->

## What Run Rules set

- **Player basics**: hearts, speed, roll.
- **Rewards**: room-clear rewards and chest chance, shop prices, traps.
- **Curse and flair.**
- **Hexed enemies** (old content; see [Elites and mini-bosses](content.md#elites-and-mini-bosses)).
- **Default hero.**
- **Offers**: which offer opens after a boss (instead of its loot, keeping its hearts, or as well), after a whole
  floor is cleared, or by chance after a room.
- **Lobby**: the lobby floor and how many starting guns and items the loadout station adds.

## Offers

An offer is a pick-N-of-M reward screen made in the **Offers** editor: how many cards are shown and picked, a
weighted pool of rewards (perk, gun upgrade, item or gun by quality, a stat change, currency, healing, heart
containers), a reroll price (+ step, max) in any currency, and what skipping gives.

Cards the hero can't use (a perk at its top level, an upgrade no held gun fits) are left out. ▶ *Try this offer* opens
it in a test room.

Offers open from:

- **Run Rules** — after a boss, when every fight room of a floor is cleared, or by chance after a room.
- **Shrines, events and items** — with the `offer` effect.
- **Mini-bosses** — the [mini-boss offer](content.md#elites-and-mini-bosses), when one is set.

## Elites

An *elite* is a normal enemy that spawns with one modifier. The modifier itself (numbers, extra patterns, aura,
tint, drops, prefix) is an asset made in the **Elite Modifiers** editor and described in
[Elites and mini-bosses](content.md#elites-and-mini-bosses). Run Rules control **how often** they appear.

**Run Rules > Elites** sets:

- the base **chance**,
- a **guaranteed** number per floor,
- whether **bosses** can be elite,
- a **chance-by-curse** curve (empty = the old hexed curve),
- a weighted **pool** of modifiers (empty = the built-in `hexed` one).

Other places add to it: a floor can add its own chance and pool in the Floor Editor, a difficulty has *Elite chance
+*, a room has *Extra elite chance in this room*, and an encounter line with **Elite** on always spawns elites (a wave
of them). Rolls use the floor's seed, so `-seed` reproduces the same elites.

**Old hexed content.** *Run Rules > Hexed enemies* still exists for content written before elite modifiers: its
numbers become the built-in `hexed` modifier (no name prefix and the old "hexed enemy appears" effect, so old enemies
look the same), and *Convert these numbers to a hexed modifier asset* turns them into a real one you can edit.

## Between runs

### Persistent currencies

In the Currency Editor, turn on *Kept between runs*. Its balance lives in the save: a new save starts with the *start
balance*, and the currency can be given while playing like any other (loot tables, offers, the `currency` effect)
plus fixed bonuses *per boss*, *per new floor* (from floor 2) and *per won run*. In a run the HUD shows it; the
balance is saved when the run ends.

A **run currency** (coins, your own) can feed one: set *Carry into*, a *Carry percent* (0-100) and what the percent is
taken of: *earned* (everything picked up this run, so spending in shops is not punished) or *held* (what is left at
the end). Banking happens on death and on a win; restarting or quitting a run banks nothing. The hero stat
`carryOver` multiplies what is banked. The preview shows an example ("a run earning 300 Coins banks 30 Glints").

### Meta upgrades

In the Upgrade Editor, set scope *meta*. Each level has a price (use a persistent currency), stats and effect blocks
like a perk, and can **open** content that stays locked until it is bought (guns, items, heroes, difficulties,
events, chests, shrines, offers, upgrades; locked content does not drop either). Levels add up and apply at the start
of every run; `WHEN run_start` blocks are the usual way to give starting coins or gear (`grant_item`, `grant_gun`).

*Requirements* make a talent tree: every listed upgrade must be owned at its level before level I can be bought.
*Group* is the column of the lobby shop and *order* the row in it. The preview draws the whole shop, with the
requirements as "needs X II".

### The lobby

A place the player walks around between runs:

1. Make a room of type **lobby** in the Room Editor. Paint station spots `1`-`9` and the exit hatch `G` (stepping
   onto it starts the run; put it away from the stations). Fill the **Stations** table: each station stands on a spot
   and either opens an **event** (a talk; a choice's *Opens screen* opens a lobby screen when the talk ends) or opens
   a **screen** directly. Label is the prompt; look is the built-in figure or prop (speaker, altar, pedestal, table,
   pillar, pot) and tint colors it; *Your sprite for this station* takes a sprite, a sheet or a motion sheet instead.
2. Make a floor with **Lobby** on in the Floor Editor: only its look (colors or tiles) and name are used; its room is
   the first lobby room in its room list, or the first lobby room.
3. Pick that floor in **Run Rules ▸ Lobby**. Empty = no lobby: the title leads to hero select and the run as before.

Screens: `meta_shop` (buy meta upgrades), `hero` (hero and difficulty for the next run), `difficulty`, `records`
(totals, unlocks, recent runs) and `loadout` (starting gear). Without a `hero` station the hero stays the last one
played; Project Check warns about it.

### Starting gear picks

Guns and items with **Start pick** on can be chosen at the loadout station (once open). They are added to the hero's
own kit: Run Rules set how many guns and items (*Start gun picks*, *Start item picks*), and a hero can set its own
numbers (-1 = Run Rules).

## Game feel

**Run Rules > Game Feel.**

- *Hit stop* freezes the world for a moment when a bullet lands (longer on a kill, an elite or a boss phase; the
  longest request wins, capped). It never fights a menu, an offer or the pause screen, and it always restores the time
  scale.
- *Damage numbers* float off the target (repeated hits on the same enemy merge for a moment, the list is capped; the
  colour separates the hero's hits from damage taken).
- *Low health* turns on under a fraction of max health (or at one heart) and pulses with an optional sound once per
  episode.
- *Aim assist* is pad-only: a target inside the cone and range pulls the aim while the mouse is never helped;
  strength 0 turns it off.
- *Shake scale* multiplies screen shake on top of the player's setting.

The crosshair comes from the Crosshair Editor (Run Rules picks one, a gun may override it); its look and the damage
numbers/low-health vignette are drawn by the UI pass and only read these rules.

## Resuming a run

A snapshot (`run.json`) is written **when a floor starts**, and the title shows CONTINUE while it exists. It stores
the seed, floor, hero, difficulty, wallets, the run's numbers, health, guns (with clip/reserve and gun upgrades),
passives/active item and perks; the floor itself is rebuilt from the seed, so enemies and opened chests are not
stored.

Death, a win and starting a new run delete it; quitting to the title keeps it, and an old version or a changed
project is refused with a message (Run Rules > Saving sets the mismatch policy). A resumed run keeps its time and
stats and counts in the records (marked as resumed). Demo and test runs never write the real save; `-run <file>`
points the tests at their own file.

## Next

- [Content and gameplay](content.md) — elite modifiers, mini-bosses, props, gates, challenge rooms.
- [Music and sound](music-sfx.md) — how Run Rules pick tracks and stingers.
- [FAQ and troubleshooting](faq.md) — Project Check, tests and common problems.
