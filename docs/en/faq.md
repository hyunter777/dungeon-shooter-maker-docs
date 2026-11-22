# FAQ and troubleshooting

This page covers testing, the project-wide check, the design rules the sample follows, and the problems people hit
most often with answers taken from the manual.

## Testing

Each editor's **▶** button starts play mode in a fitting test room with the thing you are editing: gun or item in
hand, enemy or boss in the arena, chest in a treasure room, shrine in a shrine room, hero chosen.

Built players accept the same tests on the command line, which is handy for automated checks:

```
Game.exe -testroom <room id> -gun <id> -item <id> -enemy <id> -chest <id> -shrine <id> -character <id>
         -coins N -keys N -hexed -content <json folder> -demo
```

`-difficulty <id>` plays on that difficulty; `-progress <file>` uses that save file, `-unlockall` opens everything,
`-progresstest` checks unlocks, difficulty, the save and the win screen (use a test save file). `-event <id>` puts
that event in event rooms; `-eventtest` runs a talk through the dialogue window. `-arttest` checks sounds, effect
animations and sprite slots. `-demo` plays the game by itself (moves, shoots, picks up loot).

`-autoshot file.png -shotdelay S` saves a screenshot and quits; the log lists `[event]` lines for everything that
happened (items picked, patterns fired, synergies, loot).

## Project Check

<!-- TODO(screenshot): Project Check with errors, warnings and notes, saved as assets/images/project-check.png -->

**Project Overview ▸ Check project** lists:

- **Errors**: data the game cannot load (the same messages as the editors).
- **Warnings**: content that can never appear (enemies in no floor, items nobody can get, rooms allowed on no
  floor), floors without a boss or enemies, loot tables asking for a quality no gun/item has, synergies that need
  unobtainable gear, meta upgrades that are free or priced in a run currency, persistent currencies nothing gives,
  lobby rooms without a hero station or with spot numbers that have no station. A lobby room without an exit `G` is
  an error.
- **Notes**: things that work but fall back to defaults (no shop picked, no shrine room template, one hero only).

Each line has an **Open** button that jumps to the asset.

## Design notes

- **Rewards** follow the genre's pity system: every cleared room without a chest raises the next room's chest chance
  by a step, up to a cap. Flair raises it further; curse raises mimic and hexed chances.
- **Quality** runs D, C, B, A, S. Chests, shops and loot tables pick by quality range and prefer things the player
  does not own yet.
- **Bosses** pause on an intro card, then switch states at HP thresholds; each phase can clear bullets, grant brief
  invulnerability and speed up.
- **Waves**: a normal room with *Enemy waves* > 1 spawns the next wave after the previous one is beaten.

## Automated tests

The package ships EditMode tests (`Assets/DungeonShooterMaker/Tests`): the content loads cleanly and every asset
passes its check, exporting to JSON and loading it back gives the same content, generated floors are fully connected,
and saved progress survives reloads and broken files.

Run them from **Window > General > Test Runner** (EditMode) or **Tools > Dungeon Shooter Maker > Advanced > Run
Tests**. Run them after editing content to catch broken references early.

## Troubleshooting

### My content does not load, or the game skips an entry

That is the designed behaviour: the game never loads broken data, reports the problem and skips that entry. The
editors show the same message at the top of the form. Fix the error, or read the **Errors** list in
[Project Check](#project-check).

### My JSON edit does nothing

A built game reads JSON from `Application.persistentDataPath/content/` (or a folder passed with `-content <dir>`),
and files there **override** default content by id. Check that the id in your file matches the asset you meant to
change, and that you are looking at the folder the build actually reads. See [Mods and JSON](content.md#mods-and-json).

### My drawn floor plan is ignored

A plan needs one start and one boss, every room joined, and the boss reachable without secret rooms. A broken plan is
reported by the Floor Editor and Project Check, and the floor is generated instead until it is fixed.

### A mini-boss room plays as a normal fight

An `M` room in a drawn plan, or a floor with *Mini-bosses* > 0, needs a **Mini-boss pool** (or a forced *Mini-boss*
enemy in the room). An `M` plan with an empty mini-boss pool becomes a normal fight, and Project Check shows it as an
error. See [Mini-bosses](content.md#mini-bosses).

### The hero select screen does not appear

The hero select screen needs two or more heroes. With one hero the run starts with that hero, and Project Check
notes it as a fallback.

### The lobby does not appear

**Run Rules ▸ Lobby** must name a floor made with **Lobby** on in the Floor Editor. A lobby room needs the exit hatch
`G` (missing it is an error) and a `hero` station is expected (Project Check warns without one). With the field
empty there is no lobby: the title leads to hero select and the run as usual. See
[The lobby](run-rules.md#the-lobby).

### The game is silent

No music tracks ship: the sample is silent until you add tracks in the Music Editor, and an id with no asset is
silence. For one-shot sounds, any id without a Sound asset uses the built-in generated sound. Check **Settings** for
Master, Music and Sfx volume. See [Music and sound](music-sfx.md).

### My translation does not show

An empty translation shows the original language, so a half-done translation still plays. A translation that drops or
adds a `{0}` placeholder is marked red and the original is shown instead; Project Check also warns about missing
translations and broken `{0}`s. See [Languages](content.md#languages).

### A secret room will not open

A secret room sits behind a faintly cracked wall and opens when an explosion happens near it: a bomb item, an
explosive bullet or a barrel. Opening it makes the doorway and corridor appear and the room show on the map. See
[Secret rooms](editors.md#secret-rooms).

### My 32-pixel art lost detail

*Low-res render* mode draws 32-pixel art at the game's 16-pixel grid, so fine detail is lost there. Import art at the
grid you want to see, or turn the mode off. See [Your own art](editors.md#your-own-art).

### My gun sprite sits wrong in the hand

Set the gun sprite's **Grip point** and **Muzzle point** (pixels from the sprite's top-left); -1 keeps the sprite's
pivot as the grip and fires from just in front of the hero. Guns drawn at 32 pixels per unit look big and chunky in
hand. See [Your own art](editors.md#your-own-art).

### CONTINUE is missing or the run is refused

A snapshot is written when a floor starts, and the title shows CONTINUE while it exists. Death, a win and starting a
new run delete it; quitting to the title keeps it. An old version or a changed project is refused with a message —
Run Rules > Saving sets the mismatch policy. See [Resuming a run](run-rules.md#resuming-a-run).

### An effect loops forever

Effects never start more events while they run, and bullets made by effects never count as `hit`, so blocks cannot
loop forever. If an effect seems to repeat, look at its **WHEN** event and its *Every Nth* setting in
[Effect blocks](editors.md#effect-blocks-when-if-do).

### Content never appears in a run

Project Check warns about enemies in no floor, items nobody can get, rooms allowed on no floor, loot tables asking
for a quality no gun or item has, synergies that need unobtainable gear and unlocked content that never drops. Locked
content never drops or shows up — check the Unlocks editor and any meta upgrade that opens it.
