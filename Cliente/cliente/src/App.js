import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  
} from "react-router-dom";

import Navbar  from './components/Navbar';


function App() {
  return (
    <Router>
      <Navbar/>
      <div className="container">
          <hr/>
        <Routes>
        <Route path="/" element={<h1>pagina de inicio </h1>}/>
        <Route path="/admin" element={<h1>Admin</h1>}/>
        <Route path="/login" element={<h1>login</h1>}/>
        </Routes>
      </div>
    </Router>
  );
}

export default App;


// // import React from "react";
// // import {Container, Row, Col, Card, Form, Button } from "react-bootstrap";
// // import { withRouter } from "react-router";

// // import './Styles/App.css'

// const Dash = props => {
   

//     return (
//         <>
//          <Container fluid>
//                 <Row>
//                     <Col xs={2} id="sidebar-wrapper">      
//                       <Sidebar />
//                     </Col>
//                     <Col  xs={10} id="page-content-wrapper">
//                         this is a test
//                     </Col> 
//                 </Row>

//             </Container>
//         </>
//         );
//   };
//   const Dashboard = BrowserRouter(Dash);
//   export default Dashboard

