<%@ Page Title="About Us" Language="C#" MasterPageFile="~/Site.master" AutoEventWireup="true"
	CodeBehind="Default.aspx.cs" Inherits="TexasRussellRescue.About" %>

<%@ Register Assembly="AjaxControlToolkit" Namespace="AjaxControlToolkit" TagPrefix="asp" %>
<%@ Register Src="~/SpotlightDogControl.ascx" TagName="SpotlightDogControl" TagPrefix="CustomControl" %>
<asp:Content ID="PageTitle" runat="server" ContentPlaceHolderID="PageTitle">
	<h1 class="titleText">
		Welcome</h1>
</asp:Content>
<asp:Content ID="Content1" runat="server" ContentPlaceHolderID="HeadTitle">
	Welcome
</asp:Content>
<asp:Content ID="BodyContent" runat="server" ContentPlaceHolderID="MainContent">
	<div style="padding-left: 50px; padding-right: 50px;">
	<a title="http://bit.ly/russellrescuetx"
					href="http://bit.ly/russellrescuetx"><span style="font-size:larger">Click Here: Adoption Application</span></a><br />
		<p style="padding-top: 0pt;">
			Texas Russell Rescue is the Texas group of <a onclick="window.open(this.href); return false;"
				title="http://www.russellrescue.com" href="http://www.russellrescue.com" onkeypress="window.open(this.href); return false;">
				Russell Rescue, Inc.</a> We are a network of volunteers located throughout Texas
			who are dedicated to rescuing and rehoming homeless Jack Russell Terriers. We foster
			them in our homes until we find them their perfect forever home.<div style="float: right">
				<CustomControl:SpotlightDogControl ID="spot1" runat="server" />
			</div>
			<p>
				<br />
				You will find our available dogs on the <a onclick="window.open(this.href); return false;"
					title="http://www.russellrescue.com/available-terriers/" href="http://www.russellrescue.com/available-terriers/"
					onkeypress="window.open(this.href); return false;">RRI website</a> and on Adopt-A-Pet.
				You can also see our dogs on this website by clicking on the “Available Dogs” tab
				at the top of the page.<br />
			</p>
			<p>
				If you are interested in adopting one of our dogs, please submit an <a title="http://bit.ly/russellrescuetx"
					href="http://bit.ly/russellrescuetx">adoption application.</a>
				<br />
			</p>
			<p>
				To learn more about Jack Russell’s, please read <a title="http://www.russellrescue.com/adopt/bad-dog-talk/"
					href="http://www.russellrescue.com/adopt/bad-dog-talk/">Bad Dog Talk</a>. A
				Jack Russell is not the right dog for everyone. Please read Bad Dog Talk carefully
				to see if a JR is right for you.<br />
			</p>
			<p>
				The adoption fee is $200.00. All of our JR’s are spayed/neutered, current on vaccinations,
				and on heart worm preventative. Every adopter must sign a contract agreeing that
				they will provide good care for the dog.<br />
			</p>
			<div style="align: center">
				<table>
					<tr>
						<td style="padding:50px">
							<p>
								<b>Donations Needed!</b></p>
							<table style="-moz-border-radius: 10px; -webkit-border-radius: 10px; border-radius: 10px;
								border: 1px solid; background-color: #FFFF84;">
								<tr>
									<td style="text-align: center; border-bottom: 1px solid; border-right: 1px solid">
										<b>PayPal</b>
									</td>
									<td style="text-align: center; border-bottom: 1px solid; border-left: 1px solid">
										<b>Credit Card</b>
									</td>
								</tr>
								<tr>
									<td style="text-align: center; border-top: 1px solid; border-right: 1px solid">
										Donation Type:<br />
										<asp:DropDownList ID="ddlDonation" runat="server">
											<asp:ListItem Text="General Donation" Value="General Donation"></asp:ListItem>
											<asp:ListItem Text="Owner Surrender Fee" Value="Owner Surrender Fee"></asp:ListItem>
											<asp:ListItem Text="Listing Fee" Value="Listing Fee"></asp:ListItem>
											<asp:ListItem Text="Adoption Fee" Value="Adoption Fee"></asp:ListItem>
											<asp:ListItem Text="Spotlight Terrier" Value="Spotlight"></asp:ListItem>
											<asp:ListItem Text="Memorial" Value="Memorial"></asp:ListItem>
											<asp:ListItem Text="Internet Store" Value="Store"></asp:ListItem>
										</asp:DropDownList>
										<br />
										Dog Name:<br />
										<asp:TextBox ID="txtDogName" runat="server"></asp:TextBox><br />
										<asp:ImageButton ID="ImageButton1" ImageUrl="https://www.paypal.com/en_US/i/btn/x-click-but04.gif"
											runat="server" OnClick="ImageButton1_Click" />
									</td>
									<td style="text-align: center; border-top: 1px solid; border-left: 1px solid">
										<asp:LinkButton ID="LinkButton1" runat="server" OnClick="LinkButton1_Click">Credit Card Donations</asp:LinkButton>
									</td>
								</tr>
							</table>
						</td>
		
					</tr>
				</table>
			</div>
	</div>
</asp:Content>
