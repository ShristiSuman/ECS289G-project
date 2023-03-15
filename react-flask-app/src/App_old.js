// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
	// usestate for setting a javascript
	// object for storing and using data
	const [data, setdata] = useState({
		Story: ""
	});

	// Using useEffect for single rendering
	useEffect(() => {
		// Using fetch to fetch the api from
		// flask server it will be redirected to proxy
		fetch("http://127.0.0.1:5000/data").then((res) =>
			res.json().then((data) => {
				// Setting a data from api
				setdata({
					Story: data.Story,
				});
			})
		);
	}, []);

	return (
		<div className="App">
			<header className="App-header">
				<h1>React and flask</h1>
				{/* Calling a data from setdata for showing */}
				<p>{data.Story}</p>

			</header>
		</div>
	);
}

export default App;
