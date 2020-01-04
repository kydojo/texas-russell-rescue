USE [TexasRussellRescue]
GO

/****** Object:  Table [dbo].[SpotlightDogs]    Script Date: 09/07/2012 17:37:19 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[SpotlightDogs](
	[DogID] [int] IDENTITY(2,1) NOT NULL,
	[DogName] [nvarchar](50) NULL,
	[ImagePath] [nvarchar](50) NULL,
	[Location] [nvarchar](50) NULL,
	[Sex] [nvarchar](50) NULL,
	[Age] [nvarchar](50) NULL,
	[Background] [nvarchar](max) NULL,
	[Updates] [nvarchar](max) NULL,
	[UpdateDate] [datetime] NULL
) ON [PRIMARY]

GO

