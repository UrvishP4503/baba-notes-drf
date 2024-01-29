import Profile from './components/Profile';
import SideBar from './components/SideBar';
import Notes from './components/Notes';
import './App.css';

function App() {
  return (
    <>
      <div className="container">
        <div className="left">
          <Profile />
          <SideBar />
        </div>
        <div className="right">
          <Notes />
        </div>
      </div>
    </>
  );
}

export default App;
