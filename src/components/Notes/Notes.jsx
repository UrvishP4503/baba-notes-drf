import temp from "./fetchNotes";
import "./Notes.css";

const Notes = () => {
  return temp.map(data => {
    return (
      <>
        <div className="box">
          <div className="title">{data.title}</div>
          <p className="note-text">{data.noteText}</p>
          <div className="created-at">{data.created_at}</div>
        </div>
      </>
    );
  });
};

export default Notes;
