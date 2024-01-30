import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter as Router } from "react-router-dom";
import Profile from "./components/Profile/Profile";
import SideBar from "./components/SideBar/SideBar";
import Notes from "./components/Notes/Notes";
import "./App.css";

const queryClient = new QueryClient();

function App() {
  return (
    <>
      <Router>
        <QueryClientProvider client={queryClient}>
          <div className="container">
            <div className="left">
              <Profile />
              <SideBar />
            </div>
            <div className="right">
              <Notes />
            </div>
          </div>
        </QueryClientProvider>
      </Router>
    </>
  );
}

export default App;
