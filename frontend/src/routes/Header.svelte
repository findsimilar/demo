<script>

	import {
        Collapse,
        Navbar,
        NavbarToggler,
        NavbarBrand,
        Nav,
        NavItem,
        NavLink,
        Dropdown,
        DropdownToggle,
        DropdownMenu,
        DropdownItem
  } from 'sveltestrap';

  let isOpen = false;

  function handleUpdate(event) {
    isOpen = event.detail.isOpen;
  }

</script>

<header>
  <Navbar class="navbar navbar-expand-lg fixed-top bg-primary" data-bs-theme="dark">
      <NavbarBrand href="/">demo.findsimilar.org</NavbarBrand>
      <NavbarToggler on:click={() => (isOpen = !isOpen)} />
      <Collapse {isOpen} navbar expand="md" on:update={handleUpdate}>
        <Nav navbar>
          <NavItem>
            <NavLink href="/">Home</NavLink>
          </NavItem>
          <NavItem>
            <NavLink href="/simple">Simple Usage</NavLink>
          </NavItem>
        </Nav>
      </Collapse>
    </Navbar>

</header>
