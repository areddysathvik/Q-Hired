<h1>Progress Notes</h1>
Day 1-4
        <p>Started with HRs Registration</p>
        <p>Implemented HRs Registration</p>
        <p>Found how useful the bootstrap is and base template implementation so, reimplemented Registration</p>
        <p>Implemented Log in System</p>
        <p>Found it useful to separate apps for better structuring:</p>
        <ul>
          <li><strong>Content:</strong> Shows the logged-in HR's posted jobs and also allows them to create jobs</li>
          <li><strong>Users:</strong> Registration and log in</li>
          <li><strong>Applications:</strong> Applicants can apply with job ID without any sign-in required</li>
        </ul>
<hr>
Day 5
        <p>Thought of creating a profile section giving HRs the ability to update their details</p>
<hr>
Day 6
        <p>Got weird behavior when HRs tried to update their details and after debugging found that creating additional fields in the user model was not working, so created a CustomUser model and reimplemented it</p>
        <hr>
Day 7
        <p>Implemented Applications View so that HRs can see the applications</p>
        <hr>
Day 8
        <p>For applicants to apply to various jobs, created dynamic URLs which they can do by routing to this URL "apply/job_id"</p>
        <hr>
Day 9
        <p>Found performance lag and after searching for optimizations, found the pagination concept for displaying jobs one page at a time rather than showing all jobs at once</p>
        <hr>
Day 10
        <p>Added The Resume Screening Logic so that we can provide instant Feedback about their initial Hiring Process</p>
        <hr>
