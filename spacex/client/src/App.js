import React from "react";
import "./assets/css/app.css";

import Header from "./components/header";
import Body from "./components/body";
import Footer from "./components/footer";



function App() {
  return (
    <div className="App">
      <Header/>
      <Body/>
      <Footer/>
    </div>
  );
}

export default App;
