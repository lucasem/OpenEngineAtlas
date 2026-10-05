# OpenEngineAtlas

> A curated atlas of free and open-source game engines, frameworks, specialized runtimes, and game-authoring tools.

**Last verified:** 2026-10-05  
**Entries:** 46

## Scope

This repository focuses on projects whose **engine/tool source is available under a recognized free/open-source software license**. It also includes a limited number of frameworks, interpreters, and narrative/fantasy-console tools when they are directly useful for making games; those entries are labeled by type.

A project being free to download is **not** enough by itself. Source-available projects with field-of-use or redistribution restrictions are intentionally excluded from the main list.

> Licenses listed here are summaries, not legal advice. Engines can bundle third-party libraries, assets, plugins, SDKs, console code, or export templates under different terms. Always review the upstream license files before shipping.

## Quick navigation

- [General-purpose 2D + 3D engines](#general-purpose-2d--3d-engines)
- [2D-focused engines and frameworks](#2d-focused-engines-and-frameworks)
- [3D-focused engines](#3d-focused-engines)
- [Code-first frameworks and libraries](#code-first-frameworks-and-libraries)
- [Specialized engines and authoring systems](#specialized-engines-and-authoring-systems)
- [Legacy, archived, or historical projects](#legacy-archived-or-historical-projects)
- [Projects intentionally not included](#projects-intentionally-not-included)
- [Contributing](#contributing)

<!-- BEGIN ENGINE CATALOG: generated from data/engines.json; do not edit by hand -->

## General-purpose 2D + 3D engines

Full engines capable of both 2D and 3D workflows.

| Project | Type | Focus | Main languages | License | Workflow | Website | Source |
|---|---|---|---|---|---|---|---|
| **Godot Engine** | engine | 2D + 3D | C++ engine; GDScript, C#, C++ | MIT | Visual editor + scripting | [Website](https://godotengine.org/) | [Source](https://github.com/godotengine/godot) |
| **GDevelop** | engine | 2D + 3D | TypeScript / JavaScript | MIT (core engine, IDE, extensions) | Visual/no-code events + JavaScript | [Website](https://gdevelop.io/) | [Source](https://github.com/4ian/GDevelop) |
| **Stride** | engine | 2D + 3D | C# / .NET | MIT | Visual editor + C# | [Website](https://www.stride3d.net/) | [Source](https://github.com/stride3d/stride) |
| **Bevy** | engine | 2D + 3D | Rust | MIT OR Apache-2.0 | Code-first / ECS | [Website](https://bevy.org/) | [Source](https://github.com/bevyengine/bevy) |
| **Fyrox** | engine | 2D + 3D | Rust | MIT | Visual editor + Rust | [Website](https://fyrox.rs/) | [Source](https://github.com/FyroxEngine/Fyrox) |
| **Castle Game Engine** | engine | 2D + 3D | Object Pascal | LGPL-2.0-or-later + static-linking exception | Visual editor + code | [Website](https://castle-engine.io/) | [Source](https://github.com/castle-engine/castle-engine) |
| **microStudio** | engine | 2D + 3D | microScript, JavaScript, Lua, Python | MIT | Browser/desktop editor + code | [Website](https://microstudio.dev/) | [Source](https://github.com/pmgl/microstudio) |

<details>
<summary>Notes on these entries</summary>

- **Godot Engine:** General-purpose cross-platform engine with dedicated 2D and 3D workflows.
- **GDevelop:** Accessible visual engine with 2D, 3D and multiplayer features.
- **Stride:** C# engine with a full editor; especially strong for 3D and rendering.
- **Bevy:** Data-driven ECS engine; code-first rather than editor-first.
- **Fyrox:** Rust engine with integrated scene editor and 2D/3D support.
- **Castle Game Engine:** Cross-platform 2D/3D engine with a visual editor; commercial closed-source games are supported under its exception.
- **microStudio:** Small, approachable open-source engine with online collaboration and 2D/3D capabilities.

</details>

## 2D-focused engines and frameworks

Projects primarily aimed at 2D development.

| Project | Type | Focus | Main languages | License | Workflow | Website | Source |
|---|---|---|---|---|---|---|---|
| **LÖVE** | framework | 2D | Lua / C++ | zlib | Code-first | [Website](https://love2d.org/) | [Source](https://github.com/love2d/love) |
| **HaxeFlixel** | engine | 2D | Haxe | MIT | Code-first | [Website](https://haxeflixel.com/) | [Source](https://github.com/HaxeFlixel/flixel) |
| **Solar2D** | engine | 2D | Lua / C++ | MIT | Code-first + simulator | [Website](https://solar2d.com/) | [Source](https://github.com/TRAGsoft/solar2d) |
| **Phaser** | framework | 2D | JavaScript / TypeScript | MIT | Code-first / web | [Website](https://phaser.io/) | [Source](https://github.com/phaserjs/phaser) |
| **melonJS** | engine | 2D / 2.5D | JavaScript / TypeScript | MIT | Code-first / web | [Website](https://melonjs.org/) | [Source](https://github.com/melonjs/melonJS) |
| **ct.js** | engine | 2D | JavaScript / TypeScript | MIT | Visual editor + scripting | [Website](https://ctjs.rocks/) | [Source](https://github.com/ct-js/ct-js) |
| **Orx** | engine | 2D | C / C++ | zlib | Data-driven + code | [Website](https://orx-project.org/) | [Source](https://github.com/orx/orx) |
| **Torque2D** | engine | 2D | C++ / TorqueScript | MIT | Editor + scripting | [Website](https://torque3d.org/torque2d/) | [Source](https://github.com/TorqueGameEngines/Torque2D) |

<details>
<summary>Notes on these entries</summary>

- **LÖVE:** Minimal, popular Lua framework for 2D games.
- **HaxeFlixel:** Cross-platform 2D engine built on Haxe/OpenFL.
- **Solar2D:** Formerly Corona SDK; focused on 2D mobile/desktop development.
- **Phaser:** Widely used HTML5/WebGL 2D game framework.
- **melonJS:** Lightweight web engine with tilemaps, shaders and limited 3D mesh support.
- **ct.js:** Desktop 2D engine/IDE designed to be friendly to beginners while remaining scriptable.
- **Orx:** Portable, data-driven 2D engine with a small runtime footprint.
- **Torque2D:** Dedicated 2D Torque engine with Box2D, scripting and an actively evolving editor toolset.

</details>

## 3D-focused engines

Projects primarily aimed at 3D games, simulations, or rendering-heavy applications.

| Project | Type | Focus | Main languages | License | Workflow | Website | Source |
|---|---|---|---|---|---|---|---|
| **Open 3D Engine (O3DE)** | engine | 3D | C++ / Python / Lua | Apache-2.0 | Full editor + code | [Website](https://o3de.org/) | [Source](https://github.com/o3de/o3de) |
| **jMonkeyEngine** | engine | 3D | Java | BSD-3-Clause | SDK/editor + code | [Website](https://jmonkeyengine.org/) | [Source](https://github.com/jMonkeyEngine/jmonkeyengine) |
| **Panda3D** | engine | 3D | Python / C++ | BSD-3-Clause | Code-first | [Website](https://www.panda3d.org/) | [Source](https://github.com/panda3d/panda3d) |
| **Wicked Engine** | engine | 3D | C++ / Lua | MIT | Editor + code / Lua | [Website](https://wickedengine.net/) | [Source](https://github.com/turanszkij/WickedEngine) |
| **ezEngine** | engine | 3D | C++ | MIT | Visual editor + C++ / visual scripting | [Website](https://ezengine.net/) | [Source](https://github.com/ezEngine/ezEngine) |
| **Armory3D** | engine | 3D | Haxe / C / C++ | zlib | Blender-integrated | [Website](https://armory3d.org/) | [Source](https://github.com/armory3d/armory) |
| **UPBGE** | engine | 3D | C++ / Python | GPL-3.0 | Blender-integrated | [Website](https://upbge.org/) | [Source](https://github.com/UPBGE/upbge) |
| **Torque3D** | engine | 3D | C++ / TorqueScript | MIT | Editor + scripting | [Website](https://torque3d.org/torque3d/) | [Source](https://github.com/TorqueGameEngines/Torque3D) |
| **rbfx (Rebel Fork)** | engine/framework | 3D | C++17 / experimental C# | MIT | Code-first + WYSIWYG editor | [Website](https://rebelfork.io/) | [Source](https://github.com/rbfx/rbfx) |

<details>
<summary>Notes on these entries</summary>

- **Open 3D Engine (O3DE):** Large-scale AAA-oriented 3D engine under the Linux Foundation.
- **jMonkeyEngine:** Mature Java 3D game engine and SDK.
- **Panda3D:** Mature 3D engine/framework originally developed by Disney and CMU.
- **Wicked Engine:** Modern rendering-focused 3D engine with editor and Lua scripting.
- **ezEngine:** Feature-rich C++ engine with an integrated editor; Windows is its strongest platform.
- **Armory3D:** 3D engine tightly integrated into Blender.
- **UPBGE:** Fork/continuation of the old Blender Game Engine, integrated directly into Blender.
- **Torque3D:** Long-running C++ 3D engine with networking, world tools and scripting.
- **rbfx (Rebel Fork):** Active experimental fork of Urho3D; API stability is still evolving.

</details>

## Code-first frameworks and libraries

Lower-level options for developers who prefer to build more of the game architecture themselves.

| Project | Type | Focus | Main languages | License | Workflow | Website | Source |
|---|---|---|---|---|---|---|---|
| **MonoGame** | framework | 2D + 3D | C# / .NET | MS-PL | Code-first | [Website](https://monogame.net/) | [Source](https://github.com/MonoGame/MonoGame) |
| **libGDX** | framework | 2D + 3D | Java | Apache-2.0 | Code-first | [Website](https://libgdx.com/) | [Source](https://github.com/libgdx/libgdx) |
| **Heaps** | framework | 2D + 3D | Haxe | MIT | Code-first | [Website](https://heaps.io/) | [Source](https://github.com/HeapsIO/heaps) |
| **raylib** | library/framework | 2D + 3D | C | zlib | Code-first | [Website](https://www.raylib.com/) | [Source](https://github.com/raysan5/raylib) |

<details>
<summary>Notes on these entries</summary>

- **MonoGame:** XNA-style cross-platform game framework; commonly used for custom engines and 2D games.
- **libGDX:** Cross-platform Java framework with extensive 2D/3D ecosystem.
- **Heaps:** High-performance Haxe game framework used for desktop, mobile, web and consoles.
- **raylib:** Small, approachable C library for 2D/3D game programming and teaching.

</details>

## Specialized engines and authoring systems

Genre-specific engines, narrative systems, fantasy consoles, interpreters, and domain-focused runtimes.

| Project | Type | Focus | Main languages | License | Workflow | Website | Source |
|---|---|---|---|---|---|---|---|
| **Ren'Py** | visual-novel engine | 2D / UI | Python / Ren'Py script | Mostly MIT; some LGPL components | Script-first | [Website](https://www.renpy.org/) | [Source](https://github.com/renpy/renpy) |
| **Twine** | interactive-fiction authoring tool/runtime | Text / HTML | HTML / CSS / JavaScript | GPL-3.0 | Visual story graph + web formats | [Website](https://twinery.org/) | [Source](https://github.com/klembot/twinejs) |
| **Adventure Game Studio (AGS)** | point-and-click adventure engine | 2D | C++ engine / AGS script | Artistic-2.0 | Editor + scripting | [Website](https://www.adventuregamestudio.co.uk/) | [Source](https://github.com/adventuregamestudio/ags) |
| **OpenRA** | RTS engine | 2D / isometric | C# / Lua / YAML | GPL-3.0-or-later | Mod SDK + code/data | [Website](https://www.openra.net/) | [Source](https://github.com/OpenRA/OpenRA) |
| **Recoil Engine** | RTS engine | 3D RTS | C++ / Lua | GPL-2.0 family; see project LICENSE | Engine + Lua game layer | [Website](https://recoilengine.org/) | [Source](https://github.com/beyond-all-reason/RecoilEngine) |
| **Solarus** | 2D action-RPG engine | 2D | C++ / Lua | GPL-3.0 | Quest editor + Lua | [Website](https://www.solarus-games.org/) | [Source](https://gitlab.com/solarus-games/solarus) |
| **Ikemen GO** | fighting-game engine | 2D | Go | MIT (engine); bundled assets vary | Data/script driven | [Website](https://ikemen-engine.github.io/) | [Source](https://github.com/ikemen-engine/Ikemen-GO) |
| **GB Studio** | retro handheld game creator | 2D | TypeScript / C engine | MIT | Drag-and-drop editor + scripting/plugins | [Website](https://www.gbstudio.dev/) | [Source](https://github.com/chrismaltby/gb-studio) |
| **TIC-80** | fantasy console | 2D retro | Lua, JavaScript, Ruby, Wren, Fennel, Squirrel, Janet, Python, more | MIT (core; third-party components vary) | All-in-one fantasy-console IDE | [Website](https://tic80.com/) | [Source](https://github.com/nesbox/TIC-80) |
| **WASM-4** | fantasy console | 2D retro | Any language compiling to WebAssembly | ISC | Code-first / tiny WebAssembly cartridges | [Website](https://wasm4.org/) | [Source](https://github.com/aduros/wasm4) |
| **OpenMW** | open-world RPG reimplementation engine | 3D | C++ / Lua | GPL-3.0 | Engine + editor/modding tools | [Website](https://openmw.org/) | [Source](https://gitlab.com/OpenMW/openmw) |
| **EasyRPG Player** | RPG interpreter/runtime | 2D | C++ | GPL-3.0 | Interpreter/runtime | [Website](https://easyrpg.org/) | [Source](https://github.com/EasyRPG/Player) |
| **ScummVM** | adventure/RPG interpreter framework | 2D / mixed | C++ | GPL-3.0-or-later | Engine reimplementation framework | [Website](https://www.scummvm.org/) | [Source](https://github.com/scummvm/scummvm) |
| **Yarn Spinner Core** | narrative middleware | Text / dialogue | C# / Yarn | MIT (core) | Dialogue scripting integrated into another engine | [Website](https://yarnspinner.dev/) | [Source](https://github.com/YarnSpinnerTool/YarnSpinner) |

<details>
<summary>Notes on these entries</summary>

- **Ren'Py:** Purpose-built for visual novels and choice-driven narrative games.
- **Twine:** Interactive nonlinear storytelling tool; outputs web-native stories using pluggable story formats.
- **Adventure Game Studio (AGS):** Dedicated editor and runtime for classic point-and-click adventure games.
- **OpenRA:** RTS engine centered on classic Command & Conquer-style games and total conversions.
- **Recoil Engine:** Modern continuation/fork of Spring used for large-scale RTS games such as Beyond All Reason.
- **Solarus:** Specialized 2D action-RPG engine with a graphical quest editor.
- **Ikemen GO:** Open-source fighting-game engine compatible with many M.U.G.E.N resources.
- **GB Studio:** Game Boy / Game Boy Color-oriented visual game creator and runtime toolchain.
- **TIC-80:** Fantasy computer with built-in code, sprite, map, SFX and music editors.
- **WASM-4:** Very small fantasy console for WebAssembly game cartridges.
- **OpenMW:** Open-source engine reimplementation for Morrowind; useful primarily for compatible content/modding.
- **EasyRPG Player:** Interpreter for RPG Maker 2000/2003 and EasyRPG games.
- **ScummVM:** Runs many classic adventure/RPG engines from original game data; also useful as an engine-reimplementation codebase.
- **Yarn Spinner Core:** Not a full game engine; a dedicated open-source branching dialogue compiler/runtime used inside engines.

</details>

## Legacy, archived, or historical projects

Still useful to study or maintain existing projects, but not the first recommendation for a new project.

| Project | Type | Focus | Main languages | License | Workflow | Website | Source |
|---|---|---|---|---|---|---|---|
| **Urho3D** | engine | 2D + 3D | C++ | MIT | Code + tools | [Website](https://urho3d.io/) | [Source](https://github.com/urho3d/urho3d) |
| **Cocos2d-x** | framework/engine | 2D | C++ | MIT | Code-first | [Website](https://www.cocos.com/) | [Source](https://github.com/cocos2d/cocos2d-x) |
| **Pixel Vision 8** | fantasy console | 2D retro | C# / Lua | MS-PL | Fantasy-console workflow | [Website](https://pixelvision8.github.io/) | [Source](https://github.com/PixelVision8/PixelVision8) |
| **Spring Engine (classic)** | RTS engine | 3D RTS | C++ / Lua | GPL family; see project LICENSE | Engine + Lua game layer | [Website](https://springrts.com/) | [Source](https://github.com/spring/spring) |

<details>
<summary>Notes on these entries</summary>

- **Urho3D:** Historical lightweight 2D/3D engine. Official repository was archived in 2023; active forks such as rbfx exist.
- **Cocos2d-x:** Major historical cross-platform 2D engine; upstream directs new users toward newer Cocos tooling.
- **Pixel Vision 8:** Open-source retro fantasy-console project; development appears much quieter than current alternatives such as TIC-80.
- **Spring Engine (classic):** Influential RTS engine; Recoil is a modern continuation of the Spring 105 code line.

</details>

<!-- END ENGINE CATALOG -->

## Projects intentionally not included

The main list uses a stricter FOSS definition than “free to use” or “source available.” Examples:

- **Defold** — excellent and free to use, with public source, but its current license restricts commercializing the engine itself as a competing “Game Engine Product”; Defold describes itself as **source available** rather than conventional open source. See its [license](https://defold.com/license/) and [source](https://github.com/defold/defold).
- **RPG Paper Maker** — source is public, but the project describes its main offering as free for non-commercial use, so it is not treated here as an unambiguously FOSS engine. See the [project site](https://rpg-paper-maker.com/) and [source](https://github.com/RPG-Paper-Maker/RPG-Paper-Maker).
- Proprietary engines with free tiers, such as Unity or Unreal Engine, are outside this repository’s scope.

For more detail, see [`docs/NOT_INCLUDED.md`](docs/NOT_INCLUDED.md).

## Choosing quickly

| If you want… | Start with… |
|---|---|
| A mature general-purpose editor | Godot, GDevelop, Stride |
| Rust | Bevy or Fyrox |
| C# | Stride or MonoGame |
| Java | jMonkeyEngine or libGDX |
| Python | Panda3D; Ren'Py for visual novels |
| Lua | LÖVE, Solar2D, Solarus |
| Browser-first 2D | Phaser, melonJS, microStudio |
| AAA-scale open 3D tech | O3DE |
| Blender-integrated 3D | Armory3D or UPBGE |
| RTS-specific engine | Recoil or OpenRA |
| Visual novels / interactive fiction | Ren'Py or Twine |
| Point-and-click adventures | Adventure Game Studio |
| Fighting games | Ikemen GO |
| Retro/fantasy-console constraints | TIC-80 or WASM-4 |
| Game Boy-style projects | GB Studio |

## Repository data

The canonical source of truth is [`data/engines.json`](data/engines.json). The engine catalog in this README is generated from that file. **Do not edit the generated catalog by hand.**

After changing the dataset, run:

```bash
python scripts/validate.py
python scripts/generate_readme.py
```

CI runs both validation and `python scripts/generate_readme.py --check`, so a pull request fails if the dataset is invalid or the README is stale.

## Contributing

New projects follow an **Issue → review → accepted PR → merge** workflow. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and use the **Suggest an engine or tool** issue form. Once accepted, add the project to `data/engines.json`; the README catalog is generated from that dataset.

## License

This curated repository is released under the [MIT License](LICENSE). Upstream engines remain under their own licenses.
