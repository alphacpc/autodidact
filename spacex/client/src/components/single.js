import React, {useEffect,useState} from 'react';
import { useParams } from "react-router-dom";
import { useQuery } from "@apollo/client";
import {Link} from "react-router-dom"

import {LAUNCH_ID} from "../GraphQL/Queries";


const Single = () => {

  let { flightNum } = useParams()
  flightNum = parseInt(flightNum);

  const [launch, setLaunch] = useState({})

  const { loading, error, data } = useQuery(LAUNCH_ID, {
    variables: { flight_number: flightNum },
  });


  useEffect( () => {
    
    data && setLaunch(data.launch)

  },[data])

  console.log("Le contenu dans nice launch", launch.mission_name)

  return (
    <div className="divDetail">

      <div>

        <div className='panelHead'>
          <h1>Mission : {launch.mission_name}</h1>
          <Link to="/">Retour</Link>
        </div>

        <div className="divDetailItem">
          <p>Flight Number : { launch.flight_number } </p>
          <p>Launch status : { launch.launch_success } </p>
          <p>Launch date : { launch.launch_date_local } </p>
        </div>

        <div className="divDetailItem">
          <p>Rocket name : {launch.rocket.rocket_name}</p>
          <p>Rocket type : {launch.rocket.rocket_type}</p>
        </div>


      </div>
      
    </div>
  )
}

export default Single