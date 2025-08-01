import {Link} from 'react-router-dom';
import "../css/LinkButton.css"

function LinkButton({url, buttonText}) {
    /*
        Component representing buttons that will serve as links in this application.
        The link will change the screen to whatever url is passed into the component.

        Variables:
            url - String containing the url that the button will take the user to
    */
   //TODO: Implement function for following link if clicked
   return (
        <div>
            <Link className="link-button" to={url} >{buttonText}</Link>
        </div>
   );
}

export default LinkButton;