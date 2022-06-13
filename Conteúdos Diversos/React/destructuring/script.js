
export default function Contact(props) { //Uso norma de props
    return (
        <div className="contact-card">
            <img src={props.img}/>
            <h3>{props.name}</h3>
            <div className="info-group">
                <img src="./images/phone-icon.png" />
                <p>{props.phone}</p>
            </div>
            <div className="info-group">
                <img src="./images/mail-icon.png" />
                <p>{props.email}</p>
            </div>
        </div>
    )
}

///////////////////////////////////////////////////////////////////////////////////////
/*****   DESTRUCTURING    *****/

export default function Contact({img, name, phone, email}) { //Em vez da props ser usado, entre chaves será colocado todos os atributos que a props contém
    return ( //No elemento será necessário colocar apenas o nome da propriedade sem a necessidade de colocar .props na frente
        <div className="contact-card">
            <img src={img}/>
            <h3>{name}</h3>
            <div className="info-group">
                <img src="./images/phone-icon.png" />
                <p>{phone}</p>
            </div>
            <div className="info-group">
                <img src="./images/mail-icon.png" />
                <p>{email}</p>
            </div>
        </div>
    )
}