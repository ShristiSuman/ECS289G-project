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
<li> Adaptable Author Input Module</li>
<p> A text multi-input system allows author to enter multiple attributes like genre, start of story, characters and their traits, etc to accomodate unique and creative thinking methods of different authors.</p>
<li> Story generator Module</li>
<p> The inputs fed by the user is provided as an input to GPT module which generates the initial story.</p>
<li> Dynamic Story Regeneration Editor</li>
<p> An option to edit the initial input leads to dynamic story regenration while still maintaing the crux of storyline.</p>
<li> Character Profile Creator</li>
<p> Profile creation based on </p>
<li> Character Visualizer</li>
<li> In-Game Dialogue Generator and Editor</li>
<p> Multiple optional attributes like number of characters, genre, location and expected social outcome are accomodated to  develop an in-game dialogue scene which may be edited and regenrated based on author's liking.
</ul>

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
