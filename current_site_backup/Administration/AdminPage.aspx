<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true"
	CodeBehind="AdminPage.aspx.cs" Inherits="TexasRussellRescue.Administration.AdminPage" %>

<%@ Register Assembly="Telerik.Web.UI" Namespace="Telerik.Web.UI" TagPrefix="telerik" %>
<asp:Content ID="Content1" ContentPlaceHolderID="HeadTitle" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="HeadContent" runat="server">
</asp:Content>
<asp:Content ID="Content3" ContentPlaceHolderID="PageTitle" runat="server">
	<h1 class="titleText">
		Administration Page</h1>
</asp:Content>
<asp:Content ID="Content4" ContentPlaceHolderID="MainContent" runat="server">
	<br />
	<br />
	Spotlight Dogs:
	<telerik:RadAjaxLoadingPanel ID="RadAjaxLoadingPanel1" runat="server" />
	<telerik:RadGrid ID="RadGrid1" runat="server" GridLines="None" AllowPaging="True"
		CssClass="RadGrid" AllowSorting="True" AutoGenerateColumns="False" ShowStatusBar="true"
		OnPreRender="RadGrid1_PreRender" OnNeedDataSource="RadGrid1_NeedDataSource" OnUpdateCommand="RadGrid1_UpdateCommand"
		OnInsertCommand="RadGrid1_InsertCommand" OnDeleteCommand="RadGrid1_DeleteCommand">
		<MasterTableView Width="100%" CommandItemDisplay="Top" DataKeyNames="DogID">
			<Columns>
				<telerik:GridEditCommandColumn UniqueName="EditCommandColumn">
				</telerik:GridEditCommandColumn>
				<telerik:GridBoundColumn DataField="DogID" DataType="System.Int32" FilterControlAltText="Filter DogID column"
					HeaderText="DogID" ReadOnly="True" SortExpression="DogID" UniqueName="DogID"
					ItemStyle-Width="15px">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="DogName" FilterControlAltText="Filter DogName column"
					HeaderText="DogName" SortExpression="DogName" UniqueName="DogName">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="ImagePath" FilterControlAltText="Filter ImagePath column"
					HeaderText="ImagePath" SortExpression="ImagePath" UniqueName="ImagePath">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="Location" FilterControlAltText="Filter Location column"
					HeaderText="Location" SortExpression="Location" UniqueName="Location">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="Sex" FilterControlAltText="Filter Sex column"
					HeaderText="Sex" SortExpression="Sex" UniqueName="Sex" ItemStyle-Width="15px">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="Age" FilterControlAltText="Filter Age column"
					HeaderText="Age" SortExpression="Age" UniqueName="Age">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="Background" FilterControlAltText="Filter Background column"
					HeaderText="Background" SortExpression="Background" UniqueName="Background">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="Updates" FilterControlAltText="Filter Updates column"
					HeaderText="Updates" SortExpression="Updates" UniqueName="Updates">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="UpdateDate" DataType="System.DateTime" FilterControlAltText="Filter UpdateDate column"
					HeaderText="UpdateDate" SortExpression="UpdateDate" UniqueName="UpdateDate">
				</telerik:GridBoundColumn>
				<telerik:GridButtonColumn UniqueName="DeleteColumn" Text="Delete" CommandName="Delete" />
			</Columns>
			<EditFormSettings UserControlName="SpotlightAdminControl.ascx" EditFormType="WebUserControl">
				<EditColumn UniqueName="EditCommandColumn1">
				</EditColumn>
			</EditFormSettings>
		</MasterTableView>
		<FilterMenu EnableImageSprites="False">
		</FilterMenu>
		<HeaderContextMenu CssClass="GridContextMenu GridContextMenu_Default">
		</HeaderContextMenu>
	</telerik:RadGrid>
	<asp:SqlDataSource ID="DogSqlDataSource" runat="server" ConnectionString="<%$ ConnectionStrings:TexasRussellRescueConnectionString %>"
		SelectCommand="SELECT * FROM [SpotlightDogs]"></asp:SqlDataSource>
		<br />
	<br />
	Agents:
	<telerik:RadAjaxLoadingPanel ID="RadAjaxLoadingPanel2" runat="server" />
	<telerik:RadGrid ID="RadGridAgent" runat="server" GridLines="None" AllowPaging="True"
		CssClass="RadGrid" AllowSorting="True" AutoGenerateColumns="False" ShowStatusBar="true"
		OnPreRender="RadGridAgent_PreRender" OnNeedDataSource="RadGridAgent_NeedDataSource" OnUpdateCommand="RadGridAgent_UpdateCommand"
		OnInsertCommand="RadGridAgent_InsertCommand" OnDeleteCommand="RadGridAgent_DeleteCommand">
		<MasterTableView Width="100%" CommandItemDisplay="Top" DataKeyNames="ID">
			<Columns>
				<telerik:GridEditCommandColumn UniqueName="EditCommandColumn">
				</telerik:GridEditCommandColumn>
				<telerik:GridBoundColumn DataField="ID" DataType="System.Int32" FilterControlAltText="Filter ID column"
					HeaderText="ID" ReadOnly="True" SortExpression="ID" UniqueName="ID"
					ItemStyle-Width="15px">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="Name" FilterControlAltText="Filter Name column"
					HeaderText="Name" SortExpression="Name" UniqueName="Name">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="ImagePath" FilterControlAltText="Filter ImagePath column"
					HeaderText="ImagePath" SortExpression="ImagePath" UniqueName="ImagePath">
				</telerik:GridBoundColumn>

				<telerik:GridBoundColumn DataField="Background" FilterControlAltText="Filter Background column"
					HeaderText="Background" SortExpression="Background" UniqueName="Background">
				</telerik:GridBoundColumn>
				<telerik:GridButtonColumn UniqueName="DeleteColumn" Text="Delete" CommandName="Delete" />
			</Columns>
			<EditFormSettings UserControlName="AgentAdminControl.ascx" EditFormType="WebUserControl">
				<EditColumn UniqueName="EditCommandColumn1">
				</EditColumn>
			</EditFormSettings>
		</MasterTableView>
		<FilterMenu EnableImageSprites="False">
		</FilterMenu>
		<HeaderContextMenu CssClass="GridContextMenu GridContextMenu_Default">
		</HeaderContextMenu>
	</telerik:RadGrid>
	<asp:SqlDataSource ID="AgentSqlDataSource" runat="server" ConnectionString="<%$ ConnectionStrings:TexasRussellRescueConnectionString %>"
		SelectCommand="SELECT * FROM [Agents]"></asp:SqlDataSource>
</asp:Content>
