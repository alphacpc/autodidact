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