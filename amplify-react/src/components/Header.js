import React from 'react';
import "./../assets/styles/header.css";
const Header = ({currentUser, logout}) => {

    return (
        <div className="HeaderContainer">
            Bonjour, {currentUser}
            <button onClick={logout}>Sign out</button>
        </div>
    )

}

export default Header;