import qrcode

dato="https://docs.google.com/document/d/1h6XSYbKzkxAsTM41fD41gKw7S9lrBehd/edit?usp=sharing&ouid=102432687534906608637&rtpof=true&sd=true"
qr=qrcode.make(dato)
qr.save('proyecto.png') 