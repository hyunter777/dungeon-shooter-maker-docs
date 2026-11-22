# Quick start

<!-- TODO(screenshot): Project Overview cards, saved as assets/images/overview.png -->

## 1. Open the overview

Open **Tools ▸ Dungeon Shooter Maker ▸ Project Overview**. It opens by itself the first time the package loads.

The overview shows one card per kind of content (heroes, guns, items, enemies, rooms, floors, music and so on) and
counts what the project contains. Every card opens its editor.

## 2. Play the sample

Press **▶ Play the game**. The demo scene opens and a run starts with the hero select screen.

Two or more heroes turn the hero select screen on; with one hero the run starts with that hero.

## 3. Change one value and test it

Open any editor from the overview cards, change a value and press its **▶** button to test that one thing. For
example, *▶ Try this gun* drops you in a room holding the gun; an enemy's ▶ spawns it in the arena.

<!-- TODO(screenshot): a gun in the editor with the ▶ button, saved as assets/images/editor-try.png -->

Each editor's ▶ starts play mode in a fitting test room with the thing you are editing: gun or item in hand, enemy
or boss in the arena, chest in a treasure room, shrine in a shrine room, hero chosen.

## Controls

| Input | Action |
|---|---|
| WASD | move |
| mouse | aim |
| left click | fire |
| Space | dodge roll |
| R | reload |
| Q | purge |
| F | active item |
| E | interact (buy, open, use shrine) |
| mouse wheel, Tab / 1 / 2 | switch gun |

## Where your content lives

Each piece of content is a ScriptableObject asset (`Assets/DungeonShooterMaker/Content/Default/...`) listed in the
**Content Database** (`Resources/DungeonShooterMaker/DefaultContent`). Every asset has an **id** (lower case, used
for references) and a **name** (shown to the player).

Editors check your data as you type. Problems show at the top of the form, and the game never loads broken data: it
reports the problem and skips that entry. Undo works for every edit.

See [How content works](content.md#how-content-works) for the asset model, [Mods and JSON](content.md#mods-and-json)
for the export/import folder names, and [Project Check](faq.md#project-check) for the project-wide audit.

## Next

- [The editors](editors.md) — what every window makes.
- [Run rules and progression](run-rules.md) — hearts, rewards, offers, elites, lobby.
- [Content and gameplay](content.md) — enemies, rooms, floors, props, mini-bosses.
- [Music and sound](music-sfx.md) — tracks, sounds, effect animations.
