<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true"
	CodeBehind="AdoptionApplication.aspx.cs" Inherits="TexasRussellRescue.AdoptionApplication" %>

<%@ Register Assembly="Telerik.Web.UI" Namespace="Telerik.Web.UI" TagPrefix="telerik" %>
<asp:Content ID="Content1" runat="server" ContentPlaceHolderID="HeadTitle">
	Adoption Application
</asp:Content>
<asp:Content ID="PageTitle" runat="server" ContentPlaceHolderID="PageTitle">
	<h1 class="titleText">
		Adoption Application</h1>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
	<div style="padding-left: 50px; padding-right: 50px;">		
		<p style="padding-top: 0pt;">
			Information: We endeavor to make wise and permanent placements for each terrier.
			Remember, the more conditions you make (i.e., color, coat type, age, sex and body
			type), the longer it will take! Please be open-minded to the different qualities
			that each terrier has to offer.
			<br />
			<br />
			Important Adoption Points
			<br />
			1. Rescue dogs must have containment (fence, kennel); JRTs are rarely suitable for
			city living.
			<br />
			2. We do not place terriers in homes where it must remain alone for extended periods
			of time.
			<br />
			3. We do not place dogs in homes where there are children under six years of age.
			<br />
			4. Few rescue dogs are good with cats.
			<br />
			5. Most terriers in Rescue are young adults; puppies are rarely, if ever, available.
			<br />
			6. Filling out an application does not guarantee adoption. Jack Russell Terriers
			have special needs. Not all homes are suitable for placement.
			<br />
			7. All applicants are thoroughly screened and must meet certain qualifications before
			being referred for a terrier.
			<br />
			8. Compatible terriers may not be immediately available; your patience is appreciated.
			<br />
			9. A donation to Russell Rescue, Inc. is required to adopt a terrier.
			<br />
			10. Remember, the more conditions you make (i.e., color, coat type, age, sex and
			body type), the longer it will take to find a suitable terrier to match your environment.
			<br />
			11. By submitting this application, you are making a formal request to adopt a dog
			from Russell Rescue, Inc. Please do not fill out this application if you are not
			serious about working with Russell Rescue, Inc.
			<br />
			12. If a terrier is matched to your application and placed in your home, you must
			agree to keep the terrier for at least 3 weeks (to allow time for the terrier and
			you to acclimate with each other).
			<br />
			13. We can only place terriers in homes located in the United States.
		</p>
		<asp:Label ID="Label2" runat="server" Text="Dog Information" Font-Names="Verdana"
			Font-Size="X-Large" ForeColor="Black" />
		<p>
			Adoption Preferences: In this section below, please enter your adoption preferences.
			Filling out an application does not guarantee adoption. Remember, the more conditions
			you make (i.e., color, coat type, age, sex and body type), the longer it may take
			to find a suitable terrier to match your environment.</p>
		<b>Name of terrier you would like to adopt</b><br />
		<telerik:RadTextBox Width="300px" ID="txtDogName" runat="server" EmptyMessage="UNKNOWN">
		</telerik:RadTextBox><br />
		<br />
		<b>Do you want to adopt a __________?</b><br />
		<asp:RadioButtonList ID="rblDogGender" runat="server">
			<asp:ListItem Text="Male" Value="Male"></asp:ListItem>
			<asp:ListItem Text="Female" Value="Female"></asp:ListItem>
			<asp:ListItem Text="No Preference" Value="No Preference"></asp:ListItem>
		</asp:RadioButtonList>
		<br />
		<b>Age Preference</b><br />
		<telerik:RadTextBox Width="300px" ID="txtDogAge" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>I am willing to consider a suitable dog of a different _____</b><br />
		<asp:CheckBoxList ID="chkDogDifferent" runat="server">
			<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
			<asp:ListItem Text="Different Age" Value="Different Age"></asp:ListItem>
			<asp:ListItem Text="Different Sex" Value="Different Sex"></asp:ListItem>
		</asp:CheckBoxList>
		<br />
		<b>Other Requests</b><br />
		<telerik:RadTextBox Width="300px" ID="txtDogOtherRequests" runat="server" EmptyMessage="coat type, height, weight, etc">
		</telerik:RadTextBox><br />
		<br />
		<br />
		<asp:Label ID="Label1" runat="server" Text="Applicant Information" Font-Names="Verdana"
			Font-Size="X-Large" ForeColor="Black" /><br />
		<br />
		<b>Applicant Full Name</b><br />
		<telerik:RadTextBox Width="300px" ID="txtName" runat="server" EmptyMessage="First and Last Name">
		</telerik:RadTextBox><br />
		<br />
		<b>Street Address</b><br />
		<telerik:RadTextBox Width="300px" ID="txtAddress" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>City</b><br />
		<telerik:RadTextBox Width="300px" ID="txtCity" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>State</b><br />
		<telerik:RadTextBox Width="300px" ID="txtState" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>Zip</b><br />
		<telerik:RadTextBox Width="300px" ID="txtZip" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>Email</b><br />
		<telerik:RadTextBox Width="300px" ID="txtEmail" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>Main Contact Number</b><br />
		<telerik:RadTextBox Width="300px" ID="txtMainPhone" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>Alternate Contact Number</b><br />
		<telerik:RadTextBox Width="300px" ID="txtAlternatePhone" runat="server" EmptyMessage="Please specify type and number. ie: work, home, spouse">
		</telerik:RadTextBox><br />
		<br />
		<b>Best Time to Call</b><br />
		<telerik:RadTextBox Width="300px" ID="txtTime" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>Occupation</b><br />
		<telerik:RadTextBox Width="300px" ID="txtJob" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>If approved, when could you take possession of a dog?</b><br />
		<telerik:RadTextBox Width="300px" ID="txtPossession" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>If approved, how far would you be willing to travel to pick up the terrier?</b><br />
		<telerik:RadTextBox Width="300px" ID="txtDistance" runat="server" EmptyMessage="Please specify in miles or hours">
		</telerik:RadTextBox><br />
		<br />
		<telerik:RadAjaxPanel ID="pnlAjaxRent" runat="server">
			<b>Do you own or rent your home?</b><br />
			<asp:RadioButtonList ID="rblHomeStatus" runat="server" AutoPostBack="true" OnSelectedIndexChanged="rblHomeStatus_SelectedIndexChanged">
				<asp:ListItem Text="Yes, we own the home" Value="Own"></asp:ListItem>
				<asp:ListItem Text="No, we rent the home" Value="Rent"></asp:ListItem>
			</asp:RadioButtonList>
			<br />
			<b>I (we) live in a _____</b><br />
			<asp:RadioButtonList ID="rblHomeType" runat="server">
				<asp:ListItem Text="House" Value="House"></asp:ListItem>
				<asp:ListItem Text="Apartment" Value="Apartment"></asp:ListItem>
				<asp:ListItem Text="Townhome" Value="Townhome"></asp:ListItem>
				<asp:ListItem Text="Trailer" Value="Trailer"></asp:ListItem>
			</asp:RadioButtonList>
			<asp:Panel ID="pnlRent" runat="server" Visible="false">
				<br />
				<b>If you rent, do you have your landlord's permission to own a dog?</b><br />
				<asp:RadioButtonList ID="rblLandlordPermission" runat="server">
					<asp:ListItem Text="YES" Value="YES"></asp:ListItem>
					<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
				</asp:RadioButtonList>
				<br />
				<b>Landlord's Name</b><br />
				<telerik:RadTextBox Width="300px" ID="txtLandlordName" runat="server">
				</telerik:RadTextBox><br />
				<br />
				<b>Landlord's Phone</b><br />
				<telerik:RadTextBox Width="300px" ID="txtLandlordPhone" runat="server">
				</telerik:RadTextBox>
			</asp:Panel>
		</telerik:RadAjaxPanel>
		<br />
		<br />
		<b>Do you have a completely fenced yard suitable for a dog?</b><br />
		<asp:RadioButtonList ID="rblFenced" runat="server">
			<asp:ListItem Text="YES" Value="YES"></asp:ListItem>
			<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
		</asp:RadioButtonList>
		<br />
		<b>Do you have a kennel run?</b><br />
		<asp:RadioButtonList ID="rblKennelRun" runat="server">
			<asp:ListItem Text="YES" Value="YES"></asp:ListItem>
			<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
		</asp:RadioButtonList>
		<br />
		<b>Describe fence and/or kennel run</b><br />
		<telerik:RadTextBox Width="300px" Height="150px" ID="txtDescFence" runat="server"
			TextMode="MultiLine" EmptyMessage="If none, type NONE and answer the next questions.">
		</telerik:RadTextBox><br />
		<br />
		<b>If no fence/kennel, how will you handle the dog's exercise/toilet needs?</b><br />
		<telerik:RadTextBox Width="300px" Height="150px" ID="txtToilet" runat="server" TextMode="MultiLine">
		</telerik:RadTextBox><br />
		<br />
		<b>Do you have a suitable dog crate?</b><br />
		<asp:RadioButtonList ID="rblCrate" runat="server">
			<asp:ListItem Text="YES" Value="YES"></asp:ListItem>
			<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
		</asp:RadioButtonList>
		<br />
		<b>How many adults in the household?</b><br />
		<telerik:RadTextBox Width="300px" ID="txtAdults" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>How many children in the household?</b><br />
		<telerik:RadTextBox Width="300px" ID="txtChildren" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>Are you planning to have children within the next 5 years?</b><br />
		<asp:RadioButtonList ID="rblChildren" runat="server">
			<asp:ListItem Text="YES" Value="YES"></asp:ListItem>
			<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
		</asp:RadioButtonList>
		<br />
		<b>Age of adults</b><br />
		<telerik:RadTextBox Width="300px" ID="txtAdultAge" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>Age and gender of children</b><br />
		<telerik:RadTextBox Width="300px" ID="txtChildrenDetails" runat="server" EmptyMessage="If none, type NONE.">
		</telerik:RadTextBox><br />
		<br />
		<b>Are any members of your household allergic to animals? </b>
		<br />
		<asp:RadioButtonList ID="rblAllergic" runat="server">
			<asp:ListItem Text="YES" Value="YES"></asp:ListItem>
			<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
		</asp:RadioButtonList>
		<br />
		<b>How many hours a day must the terrier be alone?</b><br />
		<telerik:RadTextBox Width="300px" ID="txtHoursAlone" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>Are there other visitors to your home, human or animal, with which a new dog will
			have to interact?</b><br />
		<asp:RadioButtonList ID="rblVisitors" runat="server">
			<asp:ListItem Text="YES" Value="YES"></asp:ListItem>
			<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
		</asp:RadioButtonList>
		<br />
		<b>How would you describe your lifestyle?</b><br />
		<asp:RadioButtonList ID="rblLifestyle" runat="server">
			<asp:ListItem Text="Very Active" Value="Very Active"></asp:ListItem>
			<asp:ListItem Text="Active" Value="Active"></asp:ListItem>
			<asp:ListItem Text="Passive" Value="Passive"></asp:ListItem>
		</asp:RadioButtonList>
		<br />
		<telerik:RadAjaxPanel ID="pnlAjaxOtherDogs" runat="server">
			<b>Do you own any other dog?</b><br />
			<asp:RadioButtonList ID="rblOtherDog" runat="server" AutoPostBack="true" OnSelectedIndexChanged="rblOwnDog_SelectedIndexChanged">
				<asp:ListItem Text="YES" Value="YES"></asp:ListItem>
				<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
			</asp:RadioButtonList>
			<asp:Panel ID="pnlOtherDogs" runat="server" Visible="false">
				<br />
				<b>Are they spayed/neutered? </b>
				<br />
				<asp:RadioButtonList ID="rblFixed" runat="server">
					<asp:ListItem Text="YES" Value="YES"></asp:ListItem>
					<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
				</asp:RadioButtonList>
				<br />
				<b>Please list breed, size, age and gender of each dog</b><br />
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
				<telerik:GridBoundColumn DataField="Breed" FilterControlAltText="Filter Breed column"
					HeaderText="Breed" SortExpression="Breed" UniqueName="Breed">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="Size" FilterControlAltText="Filter Size column"
					HeaderText="Size" SortExpression="Size" UniqueName="Size">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="Age" FilterControlAltText="Filter Age column"
					HeaderText="Age" SortExpression="Age" UniqueName="Age">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="GenderType" FilterControlAltText="Filter GenderType column"
					HeaderText="GenderType" SortExpression="GenderType" UniqueName="GenderType" ItemStyle-Width="15px">
				</telerik:GridBoundColumn>
				<telerik:GridBoundColumn DataField="Fixed" FilterControlAltText="Filter Fixed column"
					HeaderText="Fixed" SortExpression="Fixed" UniqueName="Fixed">
				</telerik:GridBoundColumn>
				<telerik:GridButtonColumn UniqueName="DeleteColumn" Text="Delete" CommandName="Delete" />
			</Columns>
			<EditFormSettings UserControlName="ApplicationDogControl.ascx" EditFormType="WebUserControl">
				<EditColumn UniqueName="EditCommandColumn1">
				</EditColumn>
			</EditFormSettings>
		</MasterTableView>
		<FilterMenu EnableImageSprites="False">
		</FilterMenu>
		<HeaderContextMenu CssClass="GridContextMenu GridContextMenu_Default">
		</HeaderContextMenu>
	</telerik:RadGrid>
				<asp:ObjectDataSource ID="GenderDataSource1" SelectMethod="GetGenders" runat="server" TypeName="TexasRussellRescue.AdoptionAppData">
				</asp:ObjectDataSource>
				<br />
			</asp:Panel>
		</telerik:RadAjaxPanel>
		<br />
		<telerik:RadAjaxPanel ID="pnlAjaxCats" runat="server">
			<b>Do you own cats? </b>
			<br />
			<asp:RadioButtonList ID="rblCats" runat="server" AutoPostBack="true" OnSelectedIndexChanged="rblCats_SelectedIndexChanged">
				<asp:ListItem Text="YES" Value="YES"></asp:ListItem>
				<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
			</asp:RadioButtonList>
			<asp:Panel ID="pnlCats" runat="server" Visible="false">
				<br />
				<b>How many cats? </b>
				<br />
				<asp:RadioButtonList ID="rblCatsCount" runat="server">
					<asp:ListItem Text="More than 3" Value="4+"></asp:ListItem>
					<asp:ListItem Text="3" Value="3"></asp:ListItem>
					<asp:ListItem Text="2" Value="2"></asp:ListItem>
					<asp:ListItem Text="1" Value="1"></asp:ListItem>
				</asp:RadioButtonList>
			</asp:Panel>
		</telerik:RadAjaxPanel>
		<br />
		<telerik:RadAjaxPanel ID="RadAjaxPanel1" runat="server">
			<b>Do you own any other animals?</b>
			<br />
			<asp:RadioButtonList ID="rblOtherAnimals" runat="server" AutoPostBack="true" OnSelectedIndexChanged="rblOtherAnimals_SelectedIndexChanged">
				<asp:ListItem Text="YES" Value="YES"></asp:ListItem>
				<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
			</asp:RadioButtonList>
			<br />
			<asp:Panel ID="pnlOtherAnimal" runat="server" Visible="false">
				<b>Please describe other animals</b><br />
				<telerik:RadTextBox Width="300px" Height="150px" TextMode="MultiLine" ID="txtOtherAnimalsDesc"
					runat="server">
				</telerik:RadTextBox><br />
			</asp:Panel>
		</telerik:RadAjaxPanel>
		<br />
		<b>How many dogs have you owned in the past 5 years?</b><br />
		<telerik:RadTextBox Width="300px" ID="txtPastDogs" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>If you know longer own the dog(s), please describe what happened to it (them). Please
			be specific.</b><br />
		<telerik:RadTextBox Width="300px" Height="150px" TextMode="MultiLine" ID="txtPastDogsDesc"
			runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>Have you ever owned a Jack Russell before?</b><br />
		<asp:RadioButtonList ID="rblJack" runat="server">
			<asp:ListItem Text="YES" Value="YES"></asp:ListItem>
			<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
		</asp:RadioButtonList>
		<br />
		<b>Why did you choose this breed?</b><br />
		<telerik:RadTextBox Width="300px" Height="150px" TextMode="MultiLine" ID="txtWhy"
			runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>Do you know what a Jack Russell is bred to do? If so, please explain.</b><br />
		<telerik:RadTextBox Width="300px" Height="150px" TextMode="MultiLine" ID="txtBred"
			runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>What activities do you plan to do with the dog?</b><br />
		<asp:CheckBoxList ID="chkActivities" runat="server" >
			<asp:ListItem Text="Pet" Value="Pet"></asp:ListItem>
			<asp:ListItem Text="Guard" Value="Guard"></asp:ListItem>
			<asp:ListItem Text="Hunting" Value="Hunting"></asp:ListItem>
			<asp:ListItem Text="Obedience" Value="Obedience"></asp:ListItem>
			<asp:ListItem Text="Terrier Trials" Value="Terrier Trials"></asp:ListItem>
			<asp:ListItem Text="Other" Value="Other"></asp:ListItem>
		</asp:CheckBoxList>
		<br />
		<b>Describe Other activity.</b><br />
		<telerik:RadTextBox Width="300px" ID="txtOtherActivity" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<b>Where do you intend to keep this dog primarily?</b><br />
		<asp:RadioButtonList ID="rblKeepDog" runat="server">
			<asp:ListItem Text="Indoors" Value="Indoors"></asp:ListItem>
			<asp:ListItem Text="Outdoors" Value="Outdoors"></asp:ListItem>
		</asp:RadioButtonList>
		<br />
		<b>Where will the dog sleep?</b><br />
		<telerik:RadTextBox Width="300px" ID="txtDogSleep" runat="server">
		</telerik:RadTextBox><br />
		<br />
		<br />
		<asp:Label ID="Label3" runat="server" Text="Veterinarian Information" Font-Names="Verdana"
			Font-Size="X-Large" ForeColor="Black" /><br />
		<br />
		<telerik:RadAjaxPanel ID="RadAjaxPanel2" runat="server">
			<b>Do you have a regular veterinarian?</b><br />
			<asp:RadioButtonList ID="rblVet" runat="server" AutoPostBack="true" OnSelectedIndexChanged="rblVet_SelectedIndexChanged">
				<asp:ListItem Text="YES" Value="YES"></asp:ListItem>
				<asp:ListItem Text="NO" Value="NO"></asp:ListItem>
			</asp:RadioButtonList>
			<asp:Panel ID="pnlVet" runat="server" Visible="false">
				<br />
				<b>Veterinarian Clinic Name</b><br />
				<telerik:RadTextBox Width="300px" ID="txtVetClinic" runat="server">
				</telerik:RadTextBox><br />
				<br />
				<b>Veterinarian Name</b><br />
				<telerik:RadTextBox Width="300px" ID="txtVetName" runat="server" EmptyMessage="First and Last Name">
				</telerik:RadTextBox><br />
				<br />
				<b>Street Address</b><br />
				<telerik:RadTextBox Width="300px" ID="txtVetAddress" runat="server">
				</telerik:RadTextBox><br />
				<br />
				<b>City</b><br />
				<telerik:RadTextBox Width="300px" ID="txtVetCity" runat="server">
				</telerik:RadTextBox><br />
				<br />
				<b>State</b><br />
				<telerik:RadTextBox Width="300px" ID="txtVetState" runat="server">
				</telerik:RadTextBox><br />
				<br />
				> <b>Zip</b><br />
				<telerik:RadTextBox Width="300px" ID="txtVetZip" runat="server">
				</telerik:RadTextBox><br />
				<br />
				<b>Veterinarian Phone Number</b><br />
				<telerik:RadTextBox Width="300px" ID="txtVetPhone" runat="server">
				</telerik:RadTextBox><br />
				<br />
				<b>Date of last visit</b><br />
				<telerik:RadTextBox Width="300px" ID="txtVetDate" runat="server">
				</telerik:RadTextBox><br />
				<br />
			</asp:Panel>
		</telerik:RadAjaxPanel>
		<br />
		<br />
		<asp:Label ID="Label4" runat="server" Text="Other Information" Font-Names="Verdana"
			Font-Size="X-Large" ForeColor="Black" /><br />
		<br />
		<b>How did you learn of Russell Rescue, Inc.?</b><br />
		<asp:RadioButtonList ID="rblFound" runat="server">
			<asp:ListItem Text="Russell Rescue, Inc. Website" Value="Russell Rescue, Inc. Website"></asp:ListItem>
			<asp:ListItem Text="JRTCA Website" Value="JRTCA Website"></asp:ListItem>
			<asp:ListItem Text="JRTCA Breeders Website" Value="JRTCA Breeders Website"></asp:ListItem>
			<asp:ListItem Text="True Grit Magazine" Value="True Grit Magazine"></asp:ListItem>
			<asp:ListItem Text="From a Breeder" Value="From a Breeder"></asp:ListItem>
			<asp:ListItem Text="From my Vet" Value="From my Vet"></asp:ListItem>
			<asp:ListItem Text="PetFinder" Value="PetFinder"></asp:ListItem>
			<asp:ListItem Text="Adopt-A-Pet" Value="Adopt-A-Pet"></asp:ListItem>
			<asp:ListItem Text="Other" Value="Other"></asp:ListItem>
		</asp:RadioButtonList>
		<br />
		<b>Personal Reference - Somone other than a family member</b><br />
		<telerik:RadTextBox Width="300px" ID="txtReference" runat="server" EmptyMessage="Name, Relationship, Phone">
		</telerik:RadTextBox><br />
		<br />
		<b>Comments</b><br />
		<telerik:RadTextBox Width="300px" ID="txtComments" Height="150px" TextMode="MultiLine"
			runat="server">
		</telerik:RadTextBox><br />
		<br />
		<telerik:RadButton ID="btnSubmit" runat="server" Text="Submit" OnClick="btnSubmit_Click">
		</telerik:RadButton>
	</div>
</asp:Content>
