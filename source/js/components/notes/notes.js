import React from 'react';
import ReactDOM from 'react-dom';
import $ from 'jquery';
import _ from 'lodash';
import moment from 'moment';

class Notes extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loadingData: true,
      loadingGroups: true,
      selectedGroup: -1,
      groups: {},
      notes: {},
      inputs: {
        description: '',
        text: '',
        group: '',
        status: '',
      },
      columns: 6
    };


    this.requestNotes = this.requestNotes.bind(this);
    this.createNewNote = this.createNewNote.bind(this);
    this.changeSelectedGroup = this.changeSelectedGroup.bind(this);
    this.requestNotes();
    this.requestGroups();
  }

  requestNotes() {
    $.ajax({
        type: 'GET',
        url: '/api/notes/',
        data: {
          data: JSON.stringify({
            filter: null
          })
        },
        success: (data) => {
          this.setState({
            notes: JSON.parse(data).notes,
            loadingData: false
          });
        }
      }
    )
  }

  requestGroups() {
    $.ajax({
        type: 'GET',
        url: '/api/notes/groups/',
        success: (data) => {
          this.setState({
            groups: JSON.parse(data),
            loadingGroups: false
          });
        }
      }
    )
  }

  createNewNote() {

    $.ajax({
      type: 'POST',
      url: '/api/notes/',
      data: {
        data: JSON.stringify({
          note: this.state.inputs
        })
      },
      success: (data)=> {
        this.requestNotes();
      }
    })
  }

  inputs() {
    return (
      <div className="">
        <div className="">
          <label >Description</label>
          <input className="content__textarea" type="text" onChange={this.inputChange.bind(this, 'description') }/>
        </div>
        <div className="">
          <label >Text</label>
          <input className="content__textarea" type="text" onChange={this.inputChange.bind(this, 'text')}/>
        </div>
        <div className="">
          <label >Group</label>
          {this.groupSelect(false, this.inputChange.bind(this, 'group'))}
        </div>
        <div className="">
          <label >Status</label>
          <input className="content__textarea" type="text" onChange={this.inputChange.bind(this, 'status')}/>
        </div>
      </div>
    )

  }

  inputChange(type, event) {

    let newState = _.extend({}, this.state.inputs);
    newState[type] = event.target.value;
    this.setState({
      inputs: newState
    });

  }

  groupSelect(addAll, onChange) {
    if (!this.state.loadingGroups) {

      let allOption;
      if (addAll) {
        allOption = <option value="-1">all</option>
      }
      return (
        <select className="content__select" onChange={onChange}>
          {Object.keys(this.state.groups).map((key)=> {
            return (
              <option value={key} key={key}>{this.state.groups[key].name}</option>
            )
          })}
          {allOption}
        </select>
      );
    }
    else {
      return (
        <select className="content__select">
          <option>groups</option>
        </select>
      );
    }
  }

  changeSelectedGroup(event) {
    console.log(event.target.value);
    this.setState({
      selectedGroup: event.target.value
    });
  }


  render() {
    let notesElement = [];
    let noteContent = (noteObject, key)=> {
      return (
        <div key={key} className='notes__note'>
          <span className='notes__note--description'>{noteObject.description}</span>
          <span className="notes__note--text">{noteObject.text}</span>
          <div><span className='notes__note--status'>{noteObject.status}</span></div>
          <div><span className='notes__note--group'>{getGroup(noteObject.group)}</span></div>
          <div><span className='notes__note--submitted'>{noteObject.submitted}</span></div>
        </div>);
    };

    let noteElement = (notesElement)=> {
      if (notesElement.length == 0) {
        return undefined;
      }
      return notesElement.map((foo)=> {
        return (<div className="note-block" style={{width:100/this.state.columns+'%'}}>{foo}</div>)
      })
    };

    let getGroup = (groupId)=> {
      if (!this.state.loadingGroups)
        return this.state.groups[groupId].name;
      else
        return groupId;
    };

    if (!this.state.loadingData) {

      for (let i = 0; i < this.state.columns; i++) {
        let index = 0;
        let temp = Object.keys(this.state.notes).reverse().map((key)=> {
          index++;
          if ((index + i) % this.state.columns == 0 && (this.state.notes[key].group == this.state.selectedGroup || this.state.selectedGroup == -1)) {
            return (noteContent(this.state.notes[key], key))
          }
          return false;

        });
        notesElement.push(temp);
      }
    }
    //console.log(notes1,notes2,notes3);
    return (<div className='notes'>
      <button onClick={this.requestNotes}>request notes</button>
      <button onClick={this.createNewNote}>new note</button>
      {this.groupSelect(true, this.changeSelectedGroup)}
      <div>{this.inputs()}</div>
      <div className="note-container">
        {noteElement(notesElement)}
      </div>
    </div>)
  }
}

export default Notes
