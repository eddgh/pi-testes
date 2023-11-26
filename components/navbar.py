# ********** Navbar ********** :

# funcoes para testar:

# Clicar na logo leva para página home
# Clicar no botão "Entrar" leva para o endpoint "signin"
# Clicar no botão "Cadastrar" leva para o endpoint "signup"
# Clicar no botão "Clique para acessar a rota" leva para o endpoint "produto/id(123123)"


# Locators

navBarLogo = '#root > nav.sc-bdnyFh.jVcacZ > main > div.sc-dlniIP.cnAMdn > img'
navBarImgSrc = '/src/assets/DDRental.png'

navBarBtnSignup = '#root > nav.sc-bdnyFh.jVcacZ > main > div.sc-eCAqax.kbjCsX > div > div > button.sc-crzpnZ.juZtYU'
navBarBtnSignupText = 'Cadastrar' 

navBarBtnSignin = '#root > nav.sc-bdnyFh.jVcacZ > main > div.sc-eCAqax.kbjCsX > div > div > button:nth-child(1)'
navBarBtnSgininText = 'Entrar'

navBarBtnAcessRoute = '#root > nav.sc-bdnyFh.jVcacZ > main > div.sc-eCAqax.kbjCsX > div > div > button:nth-child(3)'
navBarBtnAcessRouteText = 'Clique aqui para acessar a rota'