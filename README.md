# ECS289G-project
ECS289G: Computational Storytelling using AI term project (Winter 2023)

## Welcome!
* [Learn about the project](#summary-header)
* [Install the requirements](#requirements)
* [Learn more about features](#features)
* [Learn how to use it](#usage)


# Short Story Long

<p id="summary-header" align="center">Short Story Long is an automated <b>Story generating framework</b> with <b>Character Profile Creator </b> and Social interaction <b>Dialogue Generator.</b>


## Requirements

To use this repository, you need `requirements` installed. You can install it using `pip install -r requirements.txt`. Make sure that you have the last version of pip: `pip install --upgrade pip`

Install the latest version of GPT model directly from github with pip:

```bash
pip install git+https://github.com/mmabrouk/chatgpt-wrapper
```

## Features
<ul>
<li> <strong>Adaptable Author Input Module</strong></li>
<p> A text multi-input system allows author to enter multiple attributes like genre, start of story, characters and their traits, etc to accomodate unique and creative thinking methods of different authors.</p>
<li><strong> Story generator Module</strong></li>
<p> The inputs fed by the user is provided as an input to GPT module which generates the initial story.</p>
<li> <strong>Dynamic Story Regeneration Editor</strong></li>
<p> An option to edit the initial input leads to dynamic story regenration while still maintaing the crux of storyline.</p>
<li><strong> Character Profile Creator</strong></li>
<p> Profile creation based on the generated story will display character's name, age, traits and backstory. </p>
<li><strong> Character Visualizer</strong></li>
<p> Character Traits along with generated story is used as an input to GAN which results in chracter visualized as an image</p>
<li> <strong>In-Game Dialogue Generator and Editor</strong></li>
<p> Multiple optional attributes like number of characters, genre, location and expected social outcome are accomodated to  develop an in-game dialogue scene which may be edited and regenrated based on author's liking.
</ul>

## Usage

 DALLE-E is a very powerful tool which uses natural language descriptions of the scene to generate relevant images. A combination of character traits and generated story is supplied in case of this project to generate avatars of characters which are then embedded along with the profile of the character.
 
 Our project provides a complete integrated framework that can assist any author regardless of their thinking process in most idea generation or brainstorming processes involved for creating a game’s storyline, characters, appearances, in-game dialogues etc. This helps accommodate authors of different thinking characteristics on a single automated platform to help in story generation, character profile creation.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
