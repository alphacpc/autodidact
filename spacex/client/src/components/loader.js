import React from 'react';
import img_loader from "./../assets/images/loader.png";

const Loader = () => {
  return (
    <div className='divLoader'>
      <img className='imgLoader' src={img_loader} alt="Logo loader fromx spacex"/>
    </div>
  )
}

export default Loader