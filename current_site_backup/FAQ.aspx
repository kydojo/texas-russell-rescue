<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true"
	CodeBehind="FAQ.aspx.cs" Inherits="TexasRussellRescue.FAQ" %>

<asp:Content ID="Content1" runat="server" ContentPlaceHolderID="HeadTitle">
	FAQs
</asp:Content>
<asp:Content ID="PageTitle" runat="server" ContentPlaceHolderID="PageTitle">
	<h1 class="titleText">
		Frequently Asked Questions</h1>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
	<br />
	<a href="#div1">Q: How do I re-home a terrier with behavioral issues?</a><br />
	<a href="#div2">Q: I can no longer afford my terrier. Can Russell Rescue find my dog
		a new home?</a><br />
	<a href="#div3">Q: How do I re-home my senior dog?</a><br />
	<a href="#div4">Q: I saw a posting online about a terrier in need. Can you help?</a><br />
	<br />
	<br />
	<div id="div1">
		<asp:Label ID="Label1" runat="server" Text="Q: How do I re-home a terrier with behavioral issues?"
			Font-Names="Verdana" Font-Size="X-Large" ForeColor="Black" />
		<p style="padding-left: 25px">
			A: Your dog is a part of your family and we strongly suggest you do everything possible
			to keep your terrier with you. Unfortunately, thousands of Jack Russells are relinquished
			each year to shelters and rescues, where they face a very uncertain future. Many
			of these relinquishments are due to behavioral issues that are often solvable. Behavior
			problems that you can work to address without re-homing your terrier include (click
			the links for training advice):<br />
			Separation anxiety<br />
			<a href="http://www.humanesociety.org/animals/dogs/tips/separation_anxiety.html">http://www.humanesociety.org/animals/dogs/tips/separation_anxiety.html</a><br />
			Barking<br />
			<a href="http://www.humanesociety.org/animals/dogs/tips/how_to_stop_barking.html">http://www.humanesociety.org/animals/dogs/tips/how_to_stop_barking.html</a><br />
			Chewing<br />
			<a href="http://www.humanesociety.org/animals/dogs/tips/destructive_chewing.html">http://www.humanesociety.org/animals/dogs/tips/destructive_chewing.html</a><br />
			Coping with young children or a new baby<br />
			<a href="http://www.aarfatlanta.org/petsandbabies.pdf">http://www.aarfatlanta.org/petsandbabies.pdf</a><br />
			Housebreaking puppies<br />
			<a href="http://www.humanesociety.org/animals/dogs/tips/housetraining_puppies.html">
				http://www.humanesociety.org/animals/dogs/tips/housetraining_puppies.html</a><br />
			Adults and seniors<br />
			<a href="http://www.humanesociety.org/animals/dogs/tips/housetraining_adult_dogs.html">
				http://www.humanesociety.org/animals/dogs/tips/housetraining_adult_dogs.html</a><br />
			Aggression<br />
			<a href="http://www.humanesociety.org/animals/dogs/tips/aggression.html">http://www.humanesociety.org/animals/dogs/tips/aggression.html</a>
			and <a href="http://www.humanesociety.org/animals/dogs/tips/dominant_dogs.html">http://www.humanesociety.org/animals/dogs/tips/dominant_dogs.html</a><br />
			For other behavior issues and training information, please see:<br />
			<a href="http://www.humanesociety.org/animals/dogs/tips/">http://www.humanesociety.org/animals/dogs/tips/</a><br />
			<a href="http://www.ddfl.org/education/dog-behavior-tips">http://www.ddfl.org/education/dog-behavior-tips</a><br />
			<a href="http://www.petfinder.com/pet-training/surviving-dog-adolescence.html">http://www.petfinder.com/pet-training/surviving-dog-adolescence.html</a><br />
			If you are having trouble addressing your dog’s behavior issue on your own, a dog
			trainer can be helpful. Trainers often charge a very reasonable hourly fee, and
			many will provide you with a free, in-person consultation to help you determine
			whether training will help you and your dog. Finally, the reality is that shelters
			and rescues are filled with dogs seeking new homes, and the likelihood that a dog
			with unaddressed behavioral issues will make a successful transition to a new home
			is slim. Please consider that your dog is closely bonded to you and your family—and
			therefore, with persistence and positive reinforcement, you are the person most
			likely to help him/her overcome a behavioral issue.
		</p>
	</div>
	<div id="div2">
		<asp:Label ID="Label2" runat="server" Text="Q: I can no longer afford my terrier. Can Russell Rescue find my dog a new home?"
			Font-Names="Verdana" Font-Size="X-Large" ForeColor="Black" />
		<p style="padding-left: 25px">
			A: In this difficult economy, you’re not alone. Many dog owners are finding it difficult
			to care for their beloved pets. In fact, shelters and rescues are overflowing with
			dogs whose families were forced to give them up for precisely this reason. Unfortunately,
			Russell Rescue is unable to provide direct assistance to pet owners for the care
			of their terriers. However, there is help available and we strongly urge you to
			make use of every resource to keep your canine family member with you. Below you’ll
			find tips and contact information to get you started:<br />
			If you are having trouble providing for your pets’ needs (food, basic vet care,
			spaying/neutering), please see this list of low-cost resources and assistance by
			state<br />
			<a href="http://www.humanesociety.org/animals/resources/tips/trouble_affording_pet.html#Assistance_by_state">
				http://www.humanesociety.org/animals/resources/tips/trouble_affording_pet.html#Assistance_by_state</a>.
			You can also get tips on how to work with your vet to obtain the care your pet needs
			<a href="http://www.humanesociety.org/animals/resources/tips/trouble_affording_veterinary_care.html">
				http://www.humanesociety.org/animals/resources/tips/trouble_affording_veterinary_care.html</a>.
			If you have lost your home and are moving into an apartment, you can search online
			for apartments within your price range that accept dogs.<br />
			This page <a href="http://www.humanesociety.org/animals/resources/tips/animal_friendly_apartments.html">
				http://www.humanesociety.org/animals/resources/tips/animal_friendly_apartments.html</a>
			serves as a clearinghouse for information on renting with pets.
		</p>
	</div>
	<div id="div3">
		<asp:Label ID="Label3" runat="server" Text="Q: How do I re-home my senior dog?" Font-Names="Verdana"
			Font-Size="X-Large" ForeColor="Black" />
		<p style="padding-left: 25px">
			A: The harsh truth is that few adoptive homes are available to senior dogs. Dogs
			age 8 and over are particularly hard to re-home. Many people falsely assume that
			senior dogs are not the same great companions as their younger counterparts. Whatever
			the circumstance that is causing you to relinquish your pet—a long-distance move,
			a new baby, a lack of time, or just about any other issue—none will be more traumatic
			for your senior terrier than losing his or her family. Please seriously consider
			any way to make your living situation work for you and your pet. The odds that your
			senior dog will find a new loving home to live out his days are small indeed.
		</p>
	</div>
	<div id="div4">
		<asp:Label ID="Label4" runat="server" Text="Q: I saw a posting online about a terrier in need. Can you help?"
			Font-Names="Verdana" Font-Size="X-Large" ForeColor="Black" />
		<p style="padding-left: 25px">
			A: As an organization composed entirely of volunteers and funded solely by private
			donations, we unfortunately are not able to help every needy Jack Russell. However,
			as our resources permit, we take unwanted terriers into our network of foster homes.
			We receive a large number of emails about online postings. If you are contacting
			us regarding a dog you have seen or heard about online, you can help us address
			the situation in a timely and effective way by answering the following questions:
			Is the information about the dog current? On what website did you find the posting?
			Have you contacted the facility or individual that currently has the dog to verify
			the information in the posting?
		</p>
	</div>
	<p style="padding-left: 25px">
		<b>Please note that Russell Rescue of Texas is no way affiliated with any organization,
			group or business referenced above. The links listed above are provided for informational
			purposes only and should not be construed as an endorsement.</b>
	</p>
	</div>
</asp:Content>
