import React, {useEffect} from 'react';
import { useParams } from "react-router-dom";
import { useQuery } from "@apollo/client";

import {LAUNCH_ID} from "../GraphQL/Queries";


const Single = () => {

  let {flight_number} = useParams()
  // flight_number = parseInt(flight_number);
  flight_number = 2;

  const {loading, data} = useQuery(LAUNCH_ID, { variables : {flight_number:2}});


  useEffect( () => {
    
    console.log(data, "mes donnees dans single")

  },[data])


  console.log(flight_number,"Le parametre passer au url")

  return (
    <div>
      <h2>Hello world</h2>
    </div>
  )
}

export default Single