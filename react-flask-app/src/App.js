import "./App.css";

const pythonExec = () => {
    const python_code = `
     print("hello")
    `;

    const pyodide = window.pyodide;

    pyodide.runPython(python_code);
}

function App() {

	return (
		<div className="App">
			<header className="App-header">
				<h1>React and flask</h1>
				<button onClick={pythonExec}>Click</button>
			</header>
		</div>
	);
}

export default App;
