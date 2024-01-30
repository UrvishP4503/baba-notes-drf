import Dropdown from "../Dropdown/Dropdown";
import "./SideBar.css";

const SideBar = () => {
  return (
    <div className="sidebar">
      <button className="sidebar-new-note">hi</button>
      <Dropdown />
    </div>
  );
};

export default SideBar;
