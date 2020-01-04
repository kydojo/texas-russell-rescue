<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true"
	CodeBehind="Volunteer.aspx.cs" Inherits="TexasRussellRescue.Volunteer" %>
	<%@ Register Assembly="AjaxControlToolkit" Namespace="AjaxControlToolkit" TagPrefix="asp" %>
<asp:Content ID="Content1" runat="server" ContentPlaceHolderID="HeadTitle">
	We Need You!
</asp:Content>
<asp:Content ID="PageTitle" runat="server" ContentPlaceHolderID="PageTitle">
	<h1 class="titleText">
		We Need You!</h1>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
	<div style="padding-left: 50px;padding-right: 50px;">
		<p style="padding-top: 0pt;">
			Russell Rescue, Inc. is an all-volunteer organization dedicated to placing unwanted
			or abandoned Jack Russell Terriers. We have coordinators throughout the United States
			that arrange for emergency rescues and gather information designed to match appropriate
			dogs in suitable permanent and temporary homes. Volunteers are needed for everything
			from transporting dogs to fostering dogs. Our greatest need is for foster homes.
			<br />
		</p>
		<p>
			<b>Become a Foster Home</b><br />
		</p>
		<p>
			To become a foster home, please fill out a Volunteer application <span class="style">
				and</span> a <span class="style_1">Foster Home application</span>. You can even
			<span class="style_2">apply online</span>.<br />
		</p>
		<p>
			<b>Volunteer and Foster Home Applications</b><br />
		</p>
		<p>
			You can <a title="http://www.russellrescue.com/volunteer/volunteer-application/" href="http://www.russellrescue.com/volunteer/volunteer-application/"
				class="style_5">Apply Online</a>, or mail the following forms to the address below. <br />
		</p>
		<div style="float:right"><asp:Image ID="Image1" runat="server"  ImageUrl="~/myimages/Oliver.jpg" /><asp:RoundedCornersExtender ID="RoundedCornersExtender1" TargetControlID="Image1" runat="server">
			</asp:RoundedCornersExtender></div>
		<table>
			<tr>
				<td>
					Volunteer Only:
				</td>
				<td>
					Foster Home:
				</td>
			</tr>
			<tr>
				<td>
					<a title="http://www.russellrescue.com/wp-content/uploads/volunteer_app.pdf" href="http://www.russellrescue.com/wp-content/uploads/volunteer_app.pdf">
						Printable Volunteer Application</a><span class="style_4"> (PDF)<br />
				</td>
				<td>
					<a title="http://www.russellrescue.com/wp-content/uploads/volunteer_app.pdf" href="http://www.russellrescue.com/wp-content/uploads/volunteer_app.pdf">
						Printable Volunteer Application</a><span class="style_4"> (PDF)<br />
						</span>
					<br />
					<a title="http://www.russellrescue.com/wp-content/uploads/foster_home_app.pdf" href="http://www.russellrescue.com/wp-content/uploads/foster_home_app.pdf">
						Printable Foster Home Application</a><span class="style_4"> (PDF)<br />
						</span>
				</td>
			</tr>
		</table>
		<p>
			Mail to:<span class="style_3"><br />
			</span>
		</p>
		<p>
			Russell Rescue Inc.<br />
			PO Box 28<br />
			Brooklyn CT 06234<br />
		</p>
		<p>
			<b>Adopt a Terrier</b><br />
		</p>
		<p>
			You can apply to <a title="http://www.russellrescue.com/adopt/adoption-application/" href="http://www.russellrescue.com/adopt/adoption-application/"
				class="style_6">adopt</a> a Jack Russell Terrier in our network.<br />
		</p>
		<p>
			<b>Be a Responsible Breeder</b><br />
		</p>
		<p>
			If you are a breeder, you can <span class="style_7">breed responsibly</span> and
			sell your puppies only to families that understand the unique nature of the breed.<br />
		</p>
		<p>
			<b>Educate Yourself on the Breed</b><br />
		</p>
		<p>
			Learn as much as you can about this breed to make sure that the Jack Russell is
			the <a title="http://www.russellrescue.com/adopt/bad-dog-talk/" href="http://www.russellrescue.com/adopt/bad-dog-talk/"
				class="style_6">right dog for you</a>. We don't want your new terrier to end
			up back in Rescue.<br />
		</p>
		<p>
			<b>Donate to Russell Rescue, Inc.</b><br />
		</p>
		<p>
			You can <a title="http://www.russellrescue.com/donations/" href="http://www.russellrescue.com/donations/"
				class="style_6">donate</a> money to support our network. Donations are used
			for temporary housing, spaying/neutering, shipping to new homes, veterinarian treatments,
			etc.
			<br />
		</p>
		<p>
			Russell Rescue, Inc. is a 501(c)(3) charitable organization (please see the notice
			at the bottom of the home page). This means that your donations to Russell Rescue,
			Inc. are tax-deductible.
			<br />
		</p>
	</div>
</asp:Content>
