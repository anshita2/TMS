const searchfield= document.querySelector('#searchfield')
const tablehead=document.querySelector('.table-head')
const tablebody=document.querySelector(".courses-table-body")
const noResults = document.querySelector('#no-results');
const paginationContainer=document.querySelector(".pagination-container")
const tablecomplete=document.querySelector(".table-complete")
const data=tablebody.innerHTML;

// tablehead.style.display='none';
searchfield.addEventListener("keyup",(e)=>{
    const searchvalue=e.target.value.trim();
    if(searchvalue.length>0){
        paginationContainer.style.display="none"
        fetch("/courses_search",{
            body: JSON.stringify({searchtext:searchvalue}),
            method:"POST",
        })
        .then((res)=>res.json())
        .then((data)=>{
            console.log("data",data)
            tablebody.innerHTML = '';
            tablehead.style.display = 'block';
            noResults.style.display = data.length === 0 ? 'block' : 'none';
            data.forEach((courses, index) => {
                tablebody.innerHTML += `
                    <tr>
                        <td>${index + 1}</td>
                        <td>${courses.name}</td>
                        <td>${courses.duration}</td>
                        <td>${courses.start_date}</td>
                        <td>${courses.end_date}</td>
                        <td>${courses.venue_name}</td>
                        <td>${courses.trainees_enrolled}</td>
                        <td>${courses.faculty}</td>
                        <td>
                            <a href="#editEmployeeModal-${index + 1}" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                            <a href="#deleteEmployeeModal-${index + 1}" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                        </td>
                    </tr>`;
                });
        })
    }
    else {
        tablebody.innerHTML=data;
        paginationContainer.style.display="block";
    }

})