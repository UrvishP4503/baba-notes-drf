import Profile from './components/Profile';
import './App.css';

function App() {
  return (
    <>
      <div className="container">
        <div className="left">
          <Profile />
          <button className="upper">hi</button>
          <button className="lower">ho</button>
        </div>
        <div className="right">hoho</div>
      </div>
    </>
  );
}

export default App;
