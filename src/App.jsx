import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import Profile from "./components/Profile/Profile";
import SideBar from "./components/SideBar/SideBar";
import Notes from "./components/Notes/Notes";
import "./App.css";

const queryClient = new QueryClient();

function App() {
  return (
    <>
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
    </>
  );
}

export default App;
