import {gql} from "@apollo/client";

export const LAUNCHES_QUERIES = gql`
    query{
        launches{
            flight_number
            mission_name
            launch_date_local
            launch_success
        }
    }
`

export const LAUNCH_ID = gql`
    query ($flight_number: Int!){
        launch(flight_number: $flight_number){
            flight_number
            mission_name
            launch_success
            launch_year
            launch_date_local
            rocket{
                rocket_name
                rocket_type
            }
        }
    }
`
