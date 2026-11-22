# The editors

Every kind of content has its own window. This page lists what each one makes and then covers the parts they share:
your own art, room layouts and secret rooms, drawn floor plans, effect blocks, and your own effects in C#.

<!-- TODO(screenshot): the Project Overview card grid, saved as assets/images/overview.png -->

## What each window makes

| Editor | What you make |
|---|---|
| **Run Rules** | Player basics (hearts, speed, roll), room-clear rewards and chest chance, shop prices, traps, curse/flair, hexed enemies, default hero, and OFFERS: which offer opens after a boss (instead of its loot, keeping its hearts, or as well), after a whole floor is cleared, or by chance after a room. LOBBY: the lobby floor and how many starting guns and items the loadout station adds. |
| **Heroes** | Playable characters: helmet/suit colors, hearts, speed, starting guns/items/keys/coins, extra stats. Two or more heroes turn on the hero select screen. |
| **Guns** | Fire mode (semi, auto, burst, charge), clip and ammo, spread, projectiles, bounce/pierce/homing/split/explode modifiers, status effects, effect blocks while held, quality and price, tags (e.g. `pistol, ballistic`) that gun upgrades and the `gun_has_tag` condition read. Live preview. |
| **Items** | Passive items (22 stats, *mul* and *add*), effect blocks (see below), and active items with rooms/seconds/damage recharge. |
| **Synergies** | "Holding A + B (+ any N of C, D, E) gives bonus stats and reactions." Announced in game with a SYNERGY! banner. |
| **Status Effects** | Burn, poison, freeze, chill, shock and your own: damage over time, slow, stacking, duration. |
| **Enemies & Bosses** | States with movement (chase, keep range, hop, dash, teleport, orbit, wander, still) and bullet patterns (aimed, radial, random, line, summon) with repeat/rotation (spirals), acceleration, curving, wave and homing. Bosses add HP-threshold phases and an intro card. The **LIVE PATTERN** preview plays your pattern in the window; 9 presets get you started. *Elite chance ×* says whether this enemy can spawn as an elite. |
| **Elite Modifiers** | One elite prefix per enemy: health/speed/fire-delay/damage multipliers, extra bullet patterns (add to or replace the state's volleys), an aura of effect blocks, a sprite tint (outline colour/width are hooks), extra coins, hearts and loot, an appear animation and the default weight/floor range for elite pools. See [Elites and mini-bosses](content.md#elites-and-mini-bosses). |
| **Crosshairs** | Aim marker looks: sprite slot or a drawn shape (cross, ring, tee, brackets), hotspot, tint, scale, spin, recoil/recovery, hide the system cursor. Run Rules picks one; a gun can name its own. |
| **Music** | Tracks by id: a loop clip (optionally an intro), volume and loop points. Run Rules, floors, rooms, bosses and phases pick them by id; an id with no asset is silence. See [Music and sound](music-sfx.md). |
| **Sounds** | Sounds by id with one or more clips (one picked at random), volume and pitch variation. The 19 game sounds ship with recorded defaults; any id without a Sound asset uses the built-in generated sound. ▶ plays it. |
| **Effect Animations** | Animations from a sprite sheet or cut sprites: one-shot effects and looping ones (bullets, statuses). Run Rules pick one per event (34 events: shots, bullets in flight, hits, bounces, hurt, heal, death, teleport, summon, boss phase, pickups, chests, shrines, synergies, secret walls, events); guns, enemy attacks, enemies and status effects can pick their own. 42 defaults made with Pixel VFX Maker; only shell casings and dash dust are small code particles. |
| **Props** | Room props placed with one layout character: solid, bullet cover, breakable (health, loot drops, break effect blocks), flippable cover (one side stops bullets), or an exploding barrel. The four old props (T table, P pillar, O pot, X barrel) are built in. |
| **Rooms** | Paint layouts: walls of props, enemy spawns, boss and chest spots, spike traps (S), explosive barrels (X). Room type (start, normal, treasure, shop, boss, miniboss, shrine, event, secret, lobby), weight, floor range, enemy waves, and an extra elite chance. Lobby rooms add station spots 1-9, the exit hatch G and a stations table; mini-boss rooms take a spawn point (B), one forced enemy and their add waves. |
| **Floors** | Generated (room count, number of treasure/shrine/event/mini-boss/secret rooms, shop chance) or **drawn by hand** on a grid: pick a room kind, click squares, click between two rooms to join them. Enemy pool with weights per floor, boss pool, treasure chest, shop, boss loot, secret room loot, tile colors or your own floor and wall tiles. The preview shows each floor's enemy odds. *Lobby* turns a floor into the place between runs (only its look and name are used). |
| **Loot Tables** | Weighted entries (gun, item, coins, heart, ammo, key, purge, chest, nothing) with quality ranges, rolls, no-duplicates option. Used by chests, bosses, mimics and shrine challenges. |
| **Chests** | Quality, color, key cost, loot table, mimic chance and enemy, chance to break. |
| **Shops** | Shelf slots (kind + quality range or a fixed id) and a price multiplier. Prices come from Run Rules. |
| **Shrines** | Cost (coins, hearts, heart containers, keys, purges, curse, free), then instant effects (all or one at random), a lasting blessing, an item, or a challenge fight that drops a loot table. |
| **Events** | Someone to talk to in an event room: speaker name, color or your own sprite, pages of text and choices. A choice can need something (conditions, shown greyed out or hidden), cost coins/health/keys/curse, work by chance, run effect blocks, give an item or loot, start a fight, show a result line and go to another page. When the talk ends the speaker leaves, stays silent, or can be talked to again. Floors set how many event rooms they have. |
| **Currencies** | Coins and keys come built in; add your own (scrap, gems...). Name, short word in prices, icon (shape + color or your own sprite), pickup sound, HUD on/off and order, start amount, carry limit. Shop slots, shrines, event choices, chest locks and offer rerolls can cost any currency. PERSISTENCE: *Kept between runs* makes a persistent currency (start balance of a new save, bonuses per boss, new floor and won run); a run currency can carry a percent of what was earned or held into one. See [Between runs](run-rules.md#between-runs). |
| **Offers** | Pick-N-of-M reward screens: how many cards are shown and picked, a weighted pool of rewards (perk, gun upgrade, item or gun by quality, a stat change, currency, healing, heart containers), reroll price (+ step, max) in any currency, and what skipping gives. Cards the hero can't use (a perk at its top level, an upgrade no held gun fits) are left out. ▶ Try this offer opens it in a test room. Run Rules open offers after a boss, when every fight room of a floor is cleared, or by chance after a room; shrines, events and items open them with the `offer` effect. |
| **Upgrades** | Hero **perks** (for the rest of the run) and **gun upgrades** (on one gun: any gun, one gun, or every gun with a tag). Each level adds stats and effect blocks on top of the levels before it. Weight and first floor for random picks. Taken perks show in the HUD tray with their level; upgraded guns show `+N` next to their name and in the pause screen. **Meta upgrades** are bought in the lobby with a persistent currency and apply to every run: requirements (a talent tree), group (shop column) and order, a price and the content each level opens. The preview shows the whole meta shop. |
| **Difficulties** | Levels the player picks on the hero screen (▲ ▼): enemy health (also per floor and for bosses), speed, fire rate, bullet damage, extra enemies per wave, elite chance, shop prices and the hero's own stats. The first open one is the default. |
| **Unlocks** | Goals counted over all runs (runs played or won, best floor, enemies, bosses, coins, a win with a hero or on a difficulty) that open locked content: guns, items, heroes, difficulties, events, chests, shrines. Locked content never drops or shows up. The editor also shows and resets the save used when testing in the editor. |

Every list editor has **New / Duplicate / Delete / Ping**, a search box, and a preview panel on the right.

## Your own art

Guns, bullets, enemies, heroes, items and chests have a **Your sprite** slot. Leave it empty to keep the built-in
art. Fill it with a sprite sheet (PNG, set the frame width/height; frames run left to right, top to bottom) or a list
of cut sprites. More than one frame plays as an animation (enemies and heroes walk, bullets spin). Art is drawn
facing right at 16 pixels per tile whatever the import settings; the pivot is the point that sits on the object's
position. Your art keeps its own colors (the built-in shapes are tinted). There is no drawing tool: use your usual
pixel editor.

A gun sprite can give its **Grip point** (held in the hero's hand) and **Muzzle point** (where bullets and the muzzle
animation leave), in pixels from the sprite's top-left; -1 keeps the sprite's pivot as the grip and fires from just in
front of the hero. Guns drawn at 32 pixels per unit (set it in the slot) look big and chunky in hand.

### Motion sheets (Pixel Legion Maker)

Heroes and enemies can also use a motion sheet: one row per motion, with a `.json` beside the PNG naming each row
(`idle`, `running`, `attack`, `damaged`, `death`; `fps`, `frameWidth`, `frameHeight`, and the feet point `originX` /
`groundPx`). Pixel Legion Maker writes exactly this with every hero export (`Exports/Heroes/HERO_name.png` + `.json`):
drop the PNG in **Sheet** and the motions, 32 pixels per unit and the left-facing flag fill in.

The game plays idle/running from movement, attack when firing, damaged when hit and death before the body fades; a
hero's `roll` row plays during the dodge roll (the gun is put away). Missing motions fall back (running → walk →
idle). The two crowned bosses were made with Pixel Legion Maker; for heroes, export without a weapon so they hold
the game's gun.

A hero sheet can say where the gun hand is: `handX` / `handY` (pixels from a frame's top-left, drawn facing as the
sheet faces), and per row `handX` / `handY` lists (one point per frame, -1 = the sheet's point) so the gun follows the
arm. Any sheet works the same way if you write the `.json` by hand. *Low-res render* mode draws 32-pixel art at the
game's 16-pixel grid, so fine detail is lost there.

**Effects (Pixel VFX Maker).** Drop a Pixel VFX Maker export (`name.png` with `name.sheet.json` beside it) in any
sheet slot and the frame size, count, speed, looping and pivot fill in.

Floors take **floor tiles** and **wall tiles** the same way: 16x16 px each. With several frames the first is the
plain tile (used half the time) and the others are mixed in at random. Textures don't need Read/Write enabled.

## Secret rooms

A secret room sits behind a faintly cracked wall. Any explosion near the wall (a bomb item, an explosive bullet, a
barrel) opens it: the doorway and its corridor appear and the room shows on the map. Inside is a random chest, or the
floor's *secret room loot* spilled when it opens. Generated floors place *Secret rooms* of them next to plain or
special rooms (never the start or the boss room); in a drawn plan, a `?` room joined to a room is secret.

## Drawn floor plans

A drawn plan is saved as text in the floor (JSON: `layout`), one string per row. Rooms sit on even positions, `-`
joins rooms sideways and `|` up and down:

```
S-N-N
| | |
? T-B
  |
  E
```

`S` start, `N` fight, `B` boss, `T` treasure, `$` shop, `H` shrine, `E` event (a fight when no event fits), `?`
secret. Plans also use `C` for challenge rooms and `M` for mini-boss rooms.

A plan needs one start and one boss, every room joined, and the boss reachable without secret rooms. A broken plan is
reported by the Floor Editor and Project Check, and the floor is generated instead until it is fixed.

`Tools > Dungeon Shooter Maker > Advanced > Rebuild Default Sounds and Effects` recreates the default Sound and
Effect assets from `Sounds/Default` and `Vfx/Default` (your own assets are left alone).

## Effect blocks: WHEN → IF → DO

Items, synergies, guns (while held), shrines and boss phases share one system.

**WHEN** an event happens: `room_clear`, `kill`, `hit` (a player bullet hits an enemy), `damaged`, `roll`, `purge`,
`reload`, `shot`, `room_enter`, `floor_start`, `pickup` (items only), `offer_picked` (a card was taken on an offer
screen), `run_start` (once, after the hero, starting gear and meta upgrades are applied). *Chance* and *Every Nth*
thin it out; *Every Nth* counts only events whose conditions passed. Elites add `boss_kill`, `miniboss_kill` and
`elite_kill` (see [Elites and mini-bosses](content.md#elites-and-mini-bosses)).

**IF** every condition passes (each can be flipped with **NOT**): `hp_below`, `hp_full`, `coins_at_least`,
`keys_at_least`, `has` (a gun or item), `boss_room`, `enemies_at_least`, `clip_empty`, `floor_at_least`,
`stat_at_least`, `event_boss`, `upgrade_level` (a perk, or a gun upgrade on the current gun, at least level N),
`gun_has_tag`, `currency_at_least`.

**DO** the effects. Effects that pick enemies or a place have a **Target**: `event` (the enemy that was hit or
killed), `nearest`, `random`, `all`, `player`, or `source` (the boss, in phase effects). If the event's enemy already
died (a killing hit), `event` picks nobody. Effects: heal, max_hp, coins, keys, purges, ammo, reload, invulnerable,
damage, damage_room, status, status_room, explode, bullet_ring, clear_bullets, toast, `offer` (opens an offer screen),
`upgrade_gun` and `grant_perk` (a named or random one), `currency` (gives any currency), `grant_item` (a named item,
or a random one when empty), `grant_gun` (a named gun).

Boss phases offer only effects that work from a boss: bullet_ring and explode (hurt the player), damage (hurts the
player), heal (the boss), clear_bullets, toast.

Examples in the default content: *Static Coil* (WHEN hit, 20% → shock the enemy that was hit), *Last Stand Locket*
(WHEN entering a room IF below 2 hearts → 3 s invulnerable + "LAST STAND"), *Old Iron* (WHEN reloading IF the clip is
empty → ring of 8 bullets), *Gale Vulture* phase 2 (a ring of 16 bullets from the boss).

Effects never start more events while they run, and bullets made by effects never count as `hit`, so blocks cannot
loop forever.

## Your own effects in C# (no editor changes needed)

Write a class with a parameterless constructor that implements `IEffectType`, `IConditionType` or `ITriggerType`
anywhere in your project. It is found automatically and its id appears in every effect, condition and event
dropdown. See `Demo/Extensions/ExampleExtensions.cs`:

```csharp
public class ChainZapEffect : IEffectType
{
    public string Id => "chain_zap";
    public string Uses => "amount damage to the target, then jumps to count more enemies within radius";
    public string DefaultTarget => Target.Event;
    public bool SupportsHostile => false; // true = also offered in boss phases (ctx.Hostile: hurt the player)
    public void Run(ItemEffectDef e, EffectContext ctx) { /* ctx.Enemies(e.target, Target.Event), ctx.Player, ctx.Point ... */ }
}
```

`EffectContext` gives the player, the event's enemy, the event point, the room and `Enemies(target)` /
`PointOf(target)`. Fire your own event from any script with `EffectLibrary.FireTrigger("my_event")`. Ids must be
unique; clashes are listed by **Project Check**.

## Next

- [Run rules and progression](run-rules.md) — the numbers behind rewards, offers, elites and the lobby.
- [Content and gameplay](content.md) — modifiers, mini-bosses, props, pits, gates, challenge rooms and languages.
- [Music and sound](music-sfx.md) — tracks, sounds and effect animations.
