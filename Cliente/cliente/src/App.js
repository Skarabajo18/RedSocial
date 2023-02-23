import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  
} from "react-router-dom";



function App() {
  return (
    <Router>
      <div className="container">
          <hr/>
        <Routes>
        <Route path="/" element={<h1>pagina de inicio </h1>}/>
        <Route path="/contacto2" element={<h1>pagina de contacto2</h1>}/>
        <Route path="/contacto3" element={<h1>pagina de contacto3</h1>}/>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
