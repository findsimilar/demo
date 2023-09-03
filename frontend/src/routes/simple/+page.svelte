<script>
	import { Container, Form, FormGroup, Label, Button, Input } from 'sveltestrap';
	const default_separator = ','
	const films = 'Титаник,Матрица,Форрест Гамп,Терминатор 2,Гаттака,С широко закрытыми глазами,Основной инстинкт,Молчание ягнят,Зеленая миля,Достучаться до небес,Пятый элемент,Побег из Шоушенка,Телохранитель,Люди в черном,Бойцовский клуб,Один дома,Бетховен,Криминальное чтиво,Умница Уилл Хантинг,Маска,Знакомьтесь, Джо Блэк,День сурка,Большой Лебовски,Леон,Американский пирог,Шоу Трумана,Красотка,Адвокат дьявола'
</script>

<svelte:head>
	<title>Simple usage</title>
	<meta name="description" content="Simple usage example" />
</svelte:head>

<Container fluid>
   <Form method="post">
    <FormGroup>
        <Label for="text">Input text to search</Label>
        <Input id="text" name="text" placeholder="For example: Люди и глаза" />
    </FormGroup>
     <FormGroup>
        <Label for="texts">Input texts to find similars through the separator (default ,)</Label>
        <Input type="textarea" cols="40" rows="10" name="texts" id="texts" placeholder={films}/>
      </FormGroup>
       <FormGroup>
        <Label for="separator">Input separator (Default {default_separator})</Label>
        <Input id="separator" name="separator" placeholder="Separator. Default {default_separator}"  value="{default_separator}"/>
    </FormGroup>
    <Button type="button" color="primary">Find similar</Button>
  </Form>
</Container>