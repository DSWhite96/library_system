import LinkButton from "../components/LinkButton";

function Home() {
    const url = "/test";
    const content = "Test page";

    return (
        <div className="home">
            <h1>Library System</h1>
            <LinkButton url={url} buttonText={content} />
        </div>
    );
}

export default Home;