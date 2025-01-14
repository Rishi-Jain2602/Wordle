import React from 'react'
import { Link } from 'react-router-dom'
import './styles/Navbar.css'
export default function Navbar() {
  return (
    <>
    <div>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <Link className="navbar-brand mx-4" to="/">Wordle</Link>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <i className="fas fa-bars"></i> 
                    </button>

                    
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav ms-auto mb-2 mb-lg-0"> 
                            <li className="nav-item">
                                <Link className="nav-link" to="/instructions">How to Play?</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link mx-3" to="/Score">Previous Score</Link>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    </>
  )
}
