import { Link } from "react-router-dom";
import Dropdown from "../Dropdown/Dropdown";
import "./SideBar.css";

const SideBar = () => {
  return (
    <div className="sidebar">
      <Link className="sidebar-new-note" to={"/new"}>
        hi
      </Link>
      <Dropdown />
    </div>
  );
};

export default SideBar;
