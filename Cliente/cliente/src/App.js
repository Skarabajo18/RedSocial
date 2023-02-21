import Form from './Components/Registro';
import Navbar from './Components/navbar';
import Carousel from './Components/carousel';
import Card  from './Components/card';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col'

function App() {
  return (
    <div className="App">
      <Navbar/>
      <Carousel/>
      <Container>
      <Row>
      <Col xs={6} md={4}>
        <Form/>
      </Col>
      </Row>
      </Container>
      
      <Container>
      <Card/><p></p><Card/>
      </Container>
      
      
    </div>
  );
}

export default App;
