import { useState } from 'react';
import { Route, Routes } from 'react-router-dom';
import LinkButton from "./components/LinkButton";
import Home from './pages/Home';
import TestPage from './pages/TestPage';
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <main className='main-content'>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/test" element={<TestPage />} />
      </Routes>
    </main>
  )
}

export default App
