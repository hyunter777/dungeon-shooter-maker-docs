# Content and gameplay

This page covers the content model, how content gets into a build, and the gameplay pieces that are not a window of
their own: elites and mini-bosses, props, pits, gates, challenge rooms, the shopkeeper, languages and the balance
report.

<!-- TODO(screenshot): a painted room in the Room Editor, saved as assets/images/room-editor.png -->

## How content works

Each piece of content is a **ScriptableObject asset** (`Assets/DungeonShooterMaker/Content/Default/...`) listed in
the **Content Database** (`Resources/DungeonShooterMaker/DefaultContent`). Editors create, rename, duplicate and
delete these assets for you and keep the database list up to date.

- Every asset has an **id** (lower case, used for references) and a **name** (shown to the player).
- Editors check your data as you type. Problems show at the top of the form, and the game never loads broken data: it
  reports the problem and skips that entry.
- **Undo** works for every edit.
- **Project Overview ▸ Check project** finds design problems the per-asset check cannot see (see
  [Project Check](faq.md#project-check)).

## Mods and JSON

The whole database can be exported to JSON folders (**Export JSON…**) and imported back (**Import JSON…**).

A built game also reads JSON from `Application.persistentDataPath/content/` (or a folder passed with
`-content <dir>`): files there **override** default content by id, so players can mod your game without Unity.

Folder names: `guns, enemies, rooms, floors, items, statuses, loot, chests, shops, shrines, characters, synergies`
plus `ruleset.json`. The field reference is in `docs/SCHEMA.md`.

## Elites and mini-bosses

### Elite modifiers

An *elite* is a normal enemy that spawns with one modifier, made in **Tools > Dungeon Shooter Maker > Enemy Modifier
Editor**. A modifier has:

- a *prefix*, shown before the enemy name,
- multipliers for health, speed, fire delay and damage (they multiply on top of the floor difficulty, like the old
  hexed numbers),
- extra bullet patterns that join every volley ("add") or replace the state's own ("replace"),
- an *aura* of effect blocks that runs while the hero is close (the same words a boss phase uses: bullets and damage
  hit the hero, `heal` heals the elite; at most once a second),
- a sprite tint (the outline colour and width are stored for the art pass),
- extra coins, hearts and a loot table,
- an appear animation.

One modifier per enemy; bosses and mini-bosses are skipped unless you allow bosses.

### When elites appear

*Run Rules > Elites* sets the base chance, a *guaranteed* number per floor, whether bosses can be elite, a
chance-by-curse curve (empty = the old hexed curve) and a weighted **pool** of modifiers (empty = the built-in
`hexed` one).

A floor can add its own chance and pool in the Floor Editor, a difficulty has *Elite chance +*, a room has *Extra
elite chance in this room*, and an encounter line with **Elite** on always spawns elites (a wave of them). Rolls use
the floor's seed, so `-seed` reproduces the same elites.

*Run Rules > Hexed enemies* still exists for old content: its numbers become the built-in `hexed` modifier (no name
prefix and the old "hexed enemy appears" effect, so old enemies look the same), and *Convert these numbers to a
hexed modifier asset* turns them into a real one you can edit. See
[Run rules and progression](run-rules.md#elites).

### Mini-bosses

A mini-boss is **not** a boss: it is a normal enemy shown with the boss health bar.

1. Make a room of type **miniboss** (draw its spawn point with `B`).
2. Give a floor *Mini-bosses* > 0 and a *Mini-boss pool* in the Floor Editor.

It spawns with that room's waves as adds; its waves keep coming while it lives, and the room clears only after the
last add and the mini-boss are dead. It pays the **Run Rules > Offers > Mini-boss** offer, else the floor's
*Mini-boss drops* loot table (*mini-boss keeps loot* also rolls the loot when an offer is set), but it never counts as
a boss in records, unlocks or `bossDamage`.

A room can force one enemy (*Mini-boss* field). Floor plans use `M` for mini-boss rooms; an `M` plan with an empty
mini-boss pool becomes a normal fight (Project Check shows it as an error).

### Effect blocks

New words: `WHEN boss_kill / miniboss_kill / elite_kill`, `DO enemy_modifier` (id = modifier, on the target
enemies), `IF enemy_has_modifier`. See Tools > Languages for the new strings, and
[Effect blocks](editors.md#effect-blocks-when-if-do) for the system itself.

## Props, pits, gates and challenge rooms

### Props

A prop is a room-layout character with a body (**Tools > Dungeon Shooter Maker > Prop Editor**): *Layout char*
(reserved characters are refused), size, *Blocks walking* and *Stops bullets*, *Health* (0 = unbreakable), what it
drops when it breaks and the effect blocks that run then, an *Explodes* flag (the old barrel: trap radius and
damage, chains), hit/break animations and sounds, and your own sprite slot.

A **flippable** prop is cover: press E to turn it over, and with *front* blocking the flipped body only covers its
*Covered side*, so bullets from the other side pass. The old props keep their characters, so every existing room still
works: T table (flippable), P pillar, O pot (breaks in one hit), X barrel.

### Pits

Paint `~` in a room layout for a hole in the floor. Falling costs *Pit damage* hearts (a fall never kills) and puts
the hero back on the last safe square; a dodge roll crosses a one-tile pit. Enemies never step into pits. The Run
Rules set the damage, the pause and the text; the look is a placeholder tile.

### Gates

A gate locks **every door** of a room until it opens: *currency* (pay keys/coins/your own money, or hold a key item),
*floor clear* (every fight room done) or *challenge* (talking to the gate starts waves; beating them opens it). The
interaction point stands on each doorway (E from either side).

Use a gated treasure room template, or let a floor lock N treasure rooms with *Locked treasures* (their own gate,
else Run Rules > Default gate, 1 key by default); *Extra gate chance* can lock one more. A floor-clear gate on a fight
room is a trap (Project Check warns).

### Challenge rooms

A room of type **challenge** starts waves when entered: clear them within *Seconds* and without being hit (*No hit*)
to get its loot table; a failure stops the waves, pays nothing and leaves whatever is on the floor to be finished
(the room opens once it is empty). Fail can open the room, hurt, or retry once. Floors place *Challenges* in dead
ends; drawn plans use `C`.

### Shopkeeper

Give a shop a *Keeper* (an event): the shop room spawns that speaker (behind the counter by default), and talking
uses the normal event pages, choices and effects. Stealing is left to your own events.

## Languages

You write content and UI in one language (English by default). Every other language is a table that says "this text
→ its translation". **Tools > Dungeon Shooter Maker > Languages** lists every text the game shows: names,
descriptions, event dialogue, boss titles, the game title, and the UI words in code. English and Korean ship with
the package.

- **Show: Missing** lists what still needs a translation. Type it in the right column; anything left empty shows in
  the original language, so a half-done translation still plays.
- Keep `{0}`, `{1}` ... in a translation: a number or a name goes there (`{0} COINS` → `코인 {0}`). A translation
  that drops or adds one is marked red and the original is shown instead.
- **Export CSV / Import CSV** go through a spreadsheet or a translator (columns: original, translation, where it
  is).
- When you change a name or a line, its old translation becomes **Unused** and the new text **Missing**. **Remove
  unused** cleans up.
- **+ Language** adds a table. Set its code (`ja`, `de` ...): on first start the game picks the computer's language
  when there is a table for it; players change it under **Settings > Language**. Set a **Font** when the game fonts
  lack its letters (Japanese, Chinese ...).
- Your own code: show text with `Loc.T("TEXT")` or `Loc.T("{0} KEYS", n)`, and mark your own content fields
  `[Localized]`; both then appear in the window.

**Project Check** warns about missing translations and broken `{0}`s.

The game text uses the pixel font **Galmuri** (Galmuri7, Galmuri9 and Galmuri11 Bold, English and Korean), SIL Open
Font License: it may ship with your game. Change the fonts and sizes in
`Runtime/Resources/DungeonShooterMaker/UI/Game.uss`; keep pixel fonts at whole multiples of their pixel grid (the
file lists them) so they stay sharp.

## Balance

**Tools > Dungeon Shooter Maker > Balance** shows the numbers behind your content for a chosen difficulty, computed
the way the game computes them (nothing is played):

- **Coins & loot per floor**: many runs (seeds) are planned floor by floor and their rewards averaged: rooms, fights,
  enemies, coins from room clears, enemy drops and loot, coins so far, chests, keys found against keys the chests
  need, hearts, items and guns, and the average price of a shop item. A short list flags floors where keys or coins
  fall short.
- **Gun damage**: damage per shot, shots per second, damage per second over a clip and with reloads, all ammo, and
  the seconds each gun needs to kill the toughest normal enemy on each floor.
- **Enemy health & damage**: health per floor (chart and table), bullet and touch damage, bullets per second, and the
  time to kill each enemy with a chosen gun.

Shrines, events, elites and item effects are not counted; mini-boss rooms are. **Copy as CSV** puts the table on the
clipboard for a spreadsheet.

## Folder layout

```
Assets/DungeonShooterMaker/
  Runtime/        game code (Core, Actors, Combat, Dungeon, Items, UI)
  Editor/         the maker windows
  Content/Default the sample game's assets
  Resources/      the content database
  Demo/           the demo scene (play mode starts here)
  Documentation/  this guide
```

All default art is generated from small pixel maps in code (`Art.cs`, `ItemArt.cs`, `HazardArt`), so the package has
no texture dependencies. Replace sprites by editing those maps or by assigning your own sprites in code.

## Next

- [The editors](editors.md) — every window and the effect-block system.
- [Run rules and progression](run-rules.md) — chances, offers, lobby, saving.
- [FAQ and troubleshooting](faq.md) — Project Check, tests and common problems.
