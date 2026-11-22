# Music and sound

Three editors cover audio and animation: **Music** for tracks, **Sounds** for one-shot sounds, and **Effect
Animations** for the sprites that play on events. All three are picked by id from data, so nothing needs code.

<!-- TODO(screenshot): the Music editor, saved as assets/images/music.png -->

## Music

Add tracks in the Music Editor: a loop clip, an optional intro, and loop points.

Run Rules pick the title, lobby, default floor, boss, mini-boss, challenge, shop, shrine and event tracks and the
stingers (boss intro, boss defeated, victory, death, elite appears).

A floor, a room template, a boss and a boss phase can each name their own track. The ladder is:

```
phase → boss/mini-boss → room → room type → floor → default
```

Changes crossfade, the music ducks under the pause menu and offers and while a stinger plays. An id with no asset is
silence. **No tracks ship:** the sample is silent until you add them.

## Sounds

Sounds by id with one or more clips (one picked at random), volume and pitch variation.

- The **19 game sounds** ship with recorded defaults.
- Any id without a Sound asset uses the built-in generated sound.
- ▶ plays the sound in the editor.

Volumes live in **Settings**: Master, Music and Sfx (the old volume setting is the master).

## Effect Animations

Animations from a sprite sheet or cut sprites: one-shot effects and looping ones (bullets, statuses).

- **Run Rules** pick one per event: 34 events cover shots, bullets in flight, hits, bounces, hurt, heal, death,
  teleport, summon, boss phase, pickups, chests, shrines, synergies, secret walls and events.
- Guns, enemy attacks, enemies and status effects can pick their own.
- 42 defaults were made with Pixel VFX Maker; only shell casings and dash dust are small code particles.

**Rebuild defaults.** `Tools > Dungeon Shooter Maker > Advanced > Rebuild Default Sounds and Effects` recreates the
default Sound and Effect assets from `Sounds/Default` and `Vfx/Default` (your own assets are left alone).

## See also

- [The editors](editors.md) — where each id is picked.
- [Run rules and progression](run-rules.md) — the Run Rules side of music and game feel.
- [Support and licenses](support.md) — the font and sound credits that ship with the package.
