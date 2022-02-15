import React from 'react';
import logo from "./../assets/images/logo.png"

const Header = () => {
  return (
    <div className='header'>
        <a href="https://www.spacex.com/" target="_blank"><img src={logo} alt='Logo-spacex'/></a>
    </div>
  )
}

export default Header;