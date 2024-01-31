import fetchNotes from "./fetchNotes";
import "./Notes.css";

const Notes = () => {
  let temp = fetchNotes();
  return temp.map(data => {
    return (
      <div className="box" key={data.title}>
        <div className="title">{data.title}</div>
        <p className="note-text">{data.noteText}</p>
        <div className="created-at">{data.created_at}</div>
      </div>
    );
  });
};

export default Notes;
