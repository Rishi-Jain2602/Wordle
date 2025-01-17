import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import Navbar from './components/Navbar';
import Instructions from './components/Instructions';
function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/instructions' element={<Instructions/>}/>


        </Routes>
      </Router>
    </>
  );
}

export default App;
