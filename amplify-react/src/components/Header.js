import React from 'react';
import "./../assets/styles/header.css";
const Header = ({currentUser, logout}) => {

    return (
        <div className="HeaderContainer">
            <p>Bonjour {currentUser}</p>
            <button onClick={logout}>Déconnexion</button>
        </div>
    )

}

export default Header;