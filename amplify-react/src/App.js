import { Amplify } from 'aws-amplify';
import { withAuthenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';
import Header from './components/Header';
import awsExports from './aws-exports';
Amplify.configure(awsExports);

const App = ({ signOut, user }) => {

  return (
    <>
      <Header currentUser={user.username} logout={signOut}/>
      {/* <h1>Hello {user.username}</h1>
      <button onClick={signOut}>Sign out</button> */}
    </>
  );
}

export default withAuthenticator(App);