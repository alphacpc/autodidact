import React from "react";
import "./assets/css/app.css";

import {ApolloClient} from "apollo-boost";
import {ApolloProvider} from "react-apollo";

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
